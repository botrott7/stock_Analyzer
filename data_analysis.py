import os
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def load_data(file_path):
    """
    Функция для загрузки данных из CSV файла.

    Параметры:
    - file_path (str): Путь к файлу CSV.

    Возвращает:
    - data (pandas.DataFrame): Загруженные данные в виде DataFrame.
    """
    try:
        full_path = os.path.join('data', file_path)
        pd.set_option('display.float_format', '{:.3f}'.format)
        data = pd.read_csv(full_path)
        return data
    except FileNotFoundError:
        print('Файл не найден!')


def analyze_data(data):
    """
    Функция для анализа данных о ценах акций.
    Параметры:
    - data (pandas.DataFrame): Данные о ценах акций.
    Возвращает:
    - mean_price (float): Средняя закрывающая цена акции.
    - std_price (float): Стандартное отклонение цены закрытия акции.
    - correlation (float): Корреляция между ценой закрытия и объемом торгов.
    - avg_price (float): Средняя цена (по High и Low).
    - rsi (pandas.Series): Relative Strength Index (RSI) с последними 10 записями.
    - atr (pandas.Series): Average True Range (ATR) с последними 10 записями.
    """
    try:
        mean_price = data['Close'].mean()
        std_price = data['Close'].std()
        correlation = data['Close'].corr(data['Volume'])
        avg_price = (data['High'] + data['Low']).mean()

        # RSI
        delta = data['Close'].diff()
        gains = delta.clip(lower=0)
        losses = -delta.clip(upper=0)
        avg_gain = gains.rolling(window=14, min_periods=1).mean()
        avg_loss = losses.rolling(window=14, min_periods=1).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        rsi_mean_last = rsi.iloc[-10:].mean()

        # ATR
        high_low = data['High'] - data['Low']
        high_close = np.abs(data['High'] - data['Close'].shift())
        low_close = np.abs(data['Low'] - data['Close'].shift())
        ranges = pd.concat([high_low, high_close, low_close], axis=1)
        true_range = np.max(ranges, axis=1)
        atr = true_range.rolling(window=14, min_periods=1).mean()
        atr_mean_last = atr.iloc[-10:].mean()

        results = {
            'Средняя цена акции': mean_price,
            'Стандартное отклонение цены акции': std_price,
            'Корреляция между ценой акции и объемом торгов': correlation,
            'Средняя цена (по High и Low)': avg_price,
            'Средний RSI (последние 10 записей)': rsi_mean_last,
            'Средний ATR (последние 10 записей)': atr_mean_last
        }

        file_path = os.path.join('data', 'results.pickle')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            pickle.dump(results, f)

        return results
    except Exception as e:
        print("Произошла ошибка при анализе данных:", str(e))


def train_model(data):
    """
    Функция для обучения модели предсказания цены закрытия акций.
    Параметры:
    - data (pandas.DataFrame): DataFrame должен содержать столбцы
      'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'.
    Возвращает:
    - Обученная модель (LinearRegression).
    """
    try:
        # Предварительная обработка данных перед обучением
        data = data.drop('Date', axis=1)
        data['Target'] = data['Close'].shift(-1)
        data = data[:-1]  # Удаление последней строки

        X = data.drop('Target', axis=1)
        y = data['Target']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Обучение модели линейной регрессии
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Предсказания и оценка модели
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f"Mean Squared Error: {mse}")
        return model
    except KeyError:
        print("Ошибка: отсутствуют необходимые столбцы в DataFrame")


def predict_next_days(model, last_known_data, days=None):
    """
    Функция для предсказания цены акций на несколько дней вперед.
    Параметры:
    - model: Обученная модель.
    - last_known_data: Данные последнего известного дня в виде pd.Series.
    - days (int): Количество дней для предсказания.
    Возвращает:
    - Список прогнозов на указанное количество дней.
    """
    try:
        predictions = []
        current_features = last_known_data.values.reshape(1, -1)

        for _ in range(days):
            # Предсказание на следующий день
            next_day_prediction = model.predict(current_features)[0]
            predictions.append(next_day_prediction)

            # Обновляем признаки, если необходимо
            current_features = np.roll(current_features, -1)
            current_features[0, -3:] = next_day_prediction  # Предполагает, что последние 3 признака - 'Close', 'Adj Close', 'Volume'

        return predictions
    except Exception as e:
        print("Произошла ошибка:", str(e))
