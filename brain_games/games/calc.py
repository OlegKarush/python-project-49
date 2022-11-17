#!/usr/bin/env python3

import operator
import random

from brain_games.cli import beginning_range, stop_range


def get_math():
    # определяются рандомные числа
    first_number = random.randint(beginning_range, stop_range)
    second_number = random.randint(beginning_range, stop_range)
    #  определяются рандомные опеаторы
    oper = random.choice(["+", "-", "*"])
    # Задается вопрос, ввод ответа
    print(f'Question: {str(first_number)} {oper} {str(second_number)}')

    # в зависимости от оператора получаем правильный ответ
    if oper == "+":
        right_answer = operator.add(first_number, second_number)
    elif oper == "-":
        right_answer = operator.sub(first_number, second_number)
    elif oper == "*":
        right_answer = operator.mul(first_number, second_number)

    return str(right_answer)
