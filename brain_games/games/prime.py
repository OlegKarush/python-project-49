#!/usr/bin/env python3

import prompt
import random
from brain_games.cli import welcome_user


def is_prime():
    i = 3
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    # цикл ограничивает количество вопросов = 3
    while i > 0:
        # определяется рандомное число
        random_number = random.randint(1, 100)
        number_divisors = 0
        # Задается вопрос, ввод ответа
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        # Получаем правильный ответ, сравниваем ответы
        items = list(range(1, random_number + 1))
        for item in items:
            if (random_number % item) != 0:
                number_divisors += 0
            else:
                number_divisors += 1
        if number_divisors == 2:
            result = 'yes'
        else:
            result = 'no'
        if answer.lower() != result:
            return print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{result}'."
                f"\nLet's try again, {name}!")
        print('Correct!')

        i -= 1

    return print(f"Congratulations, {name}!")
