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
    count = 0 # Переменная счетчик
    min_number = 1 # Минимальное значение рассматриваемого интервала
    max_number = 100 # Максимальное значение рассматриваемого интервала
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # Загадываем рандомное число, используя генератор рандомных чисел
        predict_number = (max_number + min_number) // 2 # Сужаем интервал поиска
        if predict_number > number: # Сравниваем
            max_number = predict_number - 1
        elif predict_number < number:
            min_number = predict_number + 1
        else:
            break # Конец игры и выход из цикла
    return(count)

def score_game(random_predict) -> int:
    """ За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """

    count_ls = []
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # Загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
score_game(random_predict)


    
    