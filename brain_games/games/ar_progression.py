#!/usr/bin/env python3

import prompt
import random
from brain_games.cli import welcome_user


def find_number():
    i = 3
    name = welcome_user()
    print('What number is missing in the progression?')

    # цикл ограничивает количество вопросов = 3
    while i > 0:
        # определяются параметры арифметической прогрессии, рандомно
        number_elem = random.randint(5, 10)
        index_num = random.randint(0, number_elem - 1)
        start_num = random.randint(0, 100)
        stop_num = random.randint(210, 10000000)
        step_num = random.randint(1, 100)
        # создается список элементов прогрессии
        list_progress = list(range(start_num, stop_num, step_num)[:number_elem])
        # определяется рандомный элемент
        hidden_element = list_progress[index_num]
        # заменяется один рандомный элемент на ".."
        list_progress[index_num] = ('..')
        # печать вопроса + список элементов прогрессии
        print('Question:', end=' ')
        for num in list_progress:
            print(num, end=' ')
        answer = prompt.string('\nYour answer: ')
        # ответ пользователя проверяется на циферность, сравниваются ответы
        if answer.isnumeric():
            if int(answer) != hidden_element:
                return print(
                    f"'{answer}' is wrong answer ;(. Correct answer was 'no'."
                    f"\nLet's try again, {name}!")
            print("Correct!")
        else:
            return print(
                f"'{answer}' is wrong answer ;(. "
                f"You need to enter the numbers!\nLet's try again, {name}!")

        i -= 1

    return print(f"Congratulations, {name}!")
