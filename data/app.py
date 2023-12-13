# import csv
# import pickle
#
# def read_csv_file(file_path):
#     with open(file_path, 'r') as file:
#         csv_reader = csv.reader(file)
#         fields = next(csv_reader)  # получить заголовки столбцов
#         data = []
#         for row in csv_reader:
#             data.append(row)  # добавить все строки в список
#     return fields, data
#
# file_path = 'TSLA.csv'
# fields, data = read_csv_file(file_path)
#
# print("Заголовки столбцов:")
# print(fields)
#
# print("\nДанные:")
# s = []
# for row in data:
#     s.append(row)
#
# print(len(s))
# print(s[-1])
#
# last_data = [2023-12-12,238.550003,238.979996,233.869995,237.009995,237.009995,94809994]


# def analyze_stock(data):
#     """
#     Анализирует показатели акции.
#
#     Параметры:
#     - data (pandas.DataFrame): DataFrame, содержащий столбцы 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'.
#     Выводит:
#     - Статистические показатели и технические индикаторы.
#     """
#     # Расчет средней цены (по High и Low)
#     data['Average_Price'] = (data['High'] + data['Low']) / 2
#
#     # Расчет средней закрывающей цены
#     mean_close = data['Close'].mean()
#     print(f"Средняя цена закрытия: {mean_close}")
#
#     # Расчет стандартного отклонения цены закрытия
#     std_dev_close = data['Close'].std()
#     print(f"Стандартное отклонение цены закрытия: {std_dev_close}")
#
#     # Расчет корреляции между ценой закрытия и объемом торгов
#     correlation = data['Close'].corr(data['Volume'])
#     print(f"Корреляция между ценой закрытия и объемом: {correlation}")
#
#     # Возвращаем DataFrame с добавленными показателями
#     return data



# Подготовка исходных данных
# Для полноценной работы эти строки кода должны быть заменены на загрузку реального DataFrame
# file_1 = os.path.join(os.getcwd(), 'data', 'TSLA.csv')
# data = load_data(file_1)
#
#
# file_2 = os.path.join(os.getcwd(), 'data', 'TSLA(new).csv')
# last_data2 = load_data(file_2)
# last_data2['Target'] = last_data2['Close'].shift(-1)
# last_data2 = last_data2.iloc[:-1]
# last_data2 = last_data2.iloc[-1].drop(['Date', 'Target'])
# print(last_data2, 'Targetыыы')
#
# # Обучение модели
# model = train_model(data)
#
# # # Предсказание для последующих дней
# predictions = predict_next_days(model, last_known_data=last_data2, days=5)
# print("Predictions for the next 5 days:", predictions)