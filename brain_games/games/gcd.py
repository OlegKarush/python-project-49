#!/usr/bin/env python3

import math
import random
from brain_games.cli import beginning_range, stop_range


def find_divisor():
    # определяются рандомные числа
    number_1 = random.randint(beginning_range, stop_range)
    number_2 = random.randint(beginning_range, stop_range)
    # получаем значение максимального общего делителя
    right_answer = math.gcd(number_1, number_2)
    # Задается вопрос
    print(f'Question: {str(number_1)} {str(number_2)}')

    return str(right_answer)
