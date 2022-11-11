#!/usr/bin/env python3

import operator
import random

import prompt

from brain_games.cli import welcome_user


def exercise():
    i = 3
    name = welcome_user()
    print('What is the result of the expression?')

    # цикл ограничивает количество вопросов = 3
    while i > 0:
        # определяются рандомные числа
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        #  определяются рандомные опеаторы
        oper = random.choice(["+", "-", "*"])
        # Задается вопрос, ввод ответа
        print(f'Question: {str(number_1)} {oper} {str(number_2)}')
        answer = prompt.string('Your answer: ')

        # в зависимости от оператора производится мат.операция
        if oper == "+":
            result = operator.add(number_1, number_2)
        elif oper == "-":
            result = operator.sub(number_1, number_2)
        elif oper == "*":
            result = operator.mul(number_1, number_2)
        # сравниваются ответы
        if int(answer) == result:
            print("Correct!")
        else:
            return print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{result}'."
                f"\nLet's try again, {name}!")

        i -= 1

    return print(f"Congratulations, {name}!")
