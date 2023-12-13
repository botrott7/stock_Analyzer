import pickle


def open_result():
    try:
        with open('results.pickle', 'rb') as f:
            results = pickle.load(f)
            return results
    except FileNotFoundError:
        print('Файл не найден!')


result = open_result()

print('Средняя цена акции', result.get('Средняя цена акции'))
print('Стандартное отклонение цены акции', result.get('Стандартное отклонение цены акции'))
print('Корреляция между ценой акции и объемом торгов', result.get('Корреляция между ценой акции и объемом торгов'))
print('Средняя цена (по High и Low)', result.get('Средняя цена (по High и Low)'))
print('Средний RSI (последние 10 записей)', result.get('Средний RSI (последние 10 записей)'))
print('Средний ATR (последние 10 записей)', result.get('Средний ATR (последние 10 записей)'))
