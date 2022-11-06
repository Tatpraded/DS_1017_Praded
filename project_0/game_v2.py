"""Игра угадай число. 
Компьютер сам загадывает и угадывает число
"""
import numpy as np
def random_predict(number:int=1) -> int:
    """Компьютер угадывает рандомное число
    Args:
        number (int, optional): Загаданное число.
    Returns:
        int: Число попыток
    """
    count = 0 # переменная счетчик
    min_number = 1 # минимальное значение рассматриваемого интервала
    max_number = 100 # максимальное значение рассматриваемого интервала
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        predict_number = (max_number + min_number) // 2 # расчитываем среднее значение между min_number и max_number 
        if predict_number > number: # сравниваем загаданное значение с предполагаемым predict_number... 
            max_number = predict_number - 1 # и если оно больше уменьшаем его
        elif predict_number < number: # сравниваем загаданное значение с предполагаемым predict_number...
            min_number = predict_number + 1 # и если оно меньше увеличиваем его
            break # конец игры и выход из цикла
    return(count)

def score_game(random_predict) -> int:
    """ За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """

    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    
score_game(random_predict)


   