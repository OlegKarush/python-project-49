#!/usr/bin/env python3

import random
from brain_games.cli import beginning_range, stop_range


def is_prime():
    # определяется рандомное число
    random_number = random.randint(beginning_range, stop_range)
    number_divisors = 0
    # Задается вопрос
    print(f'Question: {random_number}')

    # Получаем правильный ответ
    items = list(range(beginning_range, random_number + 1))
    for item in items:
        if (random_number % item) != 0:
            number_divisors += 0
        else:
            number_divisors += 1
    if number_divisors == 2:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return right_answer
