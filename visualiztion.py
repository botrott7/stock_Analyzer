import matplotlib.pyplot as plt


def plot_data(data):
    fig, ax = plt.subplots(figsize=(12, 6))  # установка размера графика

    # Построение графика цены закрытия
    ax.plot(data['Date'], data['Close'], label='Close', color='blue')

    # Вычисление средней цены акции
    mean_price = data['Close'].mean()

    # Вычисление стандартного отклонения цены акции
    std_price = data['Close'].std()

    # Добавление линии среднего значения на график
    ax.axhline(mean_price, color='r', linestyle='--', label='Средняя цена')

    # Добавление линий стандартных отклонений на график
    ax.axhline(mean_price + std_price, color='g', linestyle='--', label='Средняя + 1 ст. откл.')
    ax.axhline(mean_price - std_price, color='g', linestyle='--', label='Средняя - 1 ст. откл.')

    # Добавление текста на график
    ax.text(data['Date'].iloc[-1], mean_price, f"{mean_price:.2f}", color='r')
    ax.text(data['Date'].iloc[-1], mean_price + std_price, f"{mean_price + std_price:.2f}", color='g')
    ax.text(data['Date'].iloc[-1], mean_price - std_price, f"{mean_price - std_price:.2f}", color='g')

    # Установка заголовков
    ax.set_xlabel('Дата')
    ax.set_ylabel('Цена')
    ax.set_title('Цена акции - Закрытие')
    ax.legend()

    # Форматирование оси дат
    fig.autofmt_xdate()  # Автоматический поворот дат

    # Отображение графика
    plt.tight_layout()
    plt.show()
