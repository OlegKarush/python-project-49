#!/usr/bin/env python3

import math
import prompt
import random
from brain_games.cli import welcome_user


def find_divisor():
    i = 3
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    # цикл ограничивает количество вопросов = 3
    while i > 0:
        # определяются рандомные числа
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        # получаем значение максимального общего делителя
        result = math.gcd(number_1, number_2)
        # Задается вопрос, ввод ответа
        print(f'Question: {str(number_1)} {str(number_2)}')
        answer = prompt.string('Your answer: ')

        # ответ пользователя проверяется на циферность, сравниваются ответы
        if answer.isnumeric():
            if int(answer) != result:
                return print(
                    f"'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{result}'."
                    f"\nLet's try again, {name}!")
            print("Correct!")
        else:
            return print(
                f"'{answer}' is wrong answer ;(. You need to enter the numbers!"
                f"\nLet's try again, {name}!")

        i -= 1

    return print(f"Congratulations, {name}!")
