from data_analysis import load_data, analyze_data, train_model, predict_next_days
import visualiztion
import pandas as pd


def main():
    try:
        file_data = 'TSLA.csv'
        file_new_data = 'TSLA(new).csv'
        data = load_data(file_data)
        new_data = load_data(file_new_data)
        analyze_data(data)
        new_data['Target'] = new_data['Close'].shift(-1)
        new_data = new_data.iloc[:-1]
        new_data = new_data.iloc[-1].drop(['Date', 'Target'])
        result = predict_next_days(model=train_model(data), last_known_data=new_data, days=5)
        for i, k in enumerate(result):
            print(f'Предполагаемый прогноз на {i + 1} день составляет: {round(k, 2)}')
        data['Date'] = pd.to_datetime(data['Date'])
        visualiztion.plot_data(data)
        print('END')
    except FileNotFoundError:
        print("Ошибка: файл не найден")
    except KeyError:
        print("Ошибка: отсутствуют необходимые столбцы в DataFrame")


if __name__ == '__main__':
    print('START')
    main()
