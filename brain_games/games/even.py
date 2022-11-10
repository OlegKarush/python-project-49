#!/usr/bin/env python3

import prompt
import random
from brain_games.cli import welcome_user


def determine_even_number():
    i = 3
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    # цикл ограничивает количество вопросов = 3
    while i > 0:
        # определяются рандомные числа
        random_number = random.randint(1, 100)
        # Задается вопрос, ввод ответа
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        # Получаем правильный ответ, сравниваем ответы
        if random_number % 2 == 0:
            if answer.lower() != 'yes':
                return print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            print('Correct!')
        elif random_number % 2 != 0:
            if answer.lower() != 'no':
                return print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            print('Correct!')

        i -= 1

    return print(f"Congratulations, {name}!")
