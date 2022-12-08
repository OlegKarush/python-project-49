#!/usr/bin/env python3

import prompt

# констаны для движка игры
NUM_OF_ROUNDS = 3


# приветствуем игрока
def greeting():
    print('Welcome to the Brain Games!')


# запрашиваем имя
def welcome_user():
    get_name = prompt.string('May I have your name? ')
    print(f'Hello, {get_name.capitalize()}!')
    return get_name.capitalize()


# сравниваем правильный ответ и ответ игрока
def comparison_responses(answer, right_answer, name):
    if answer.lower() == str(right_answer):
        print('Correct!')
    else:
        print(
            f'\'{answer}\' is wrong answer ;(. '
            f'Correct answer was \'{right_answer}\'.'
            f'\nLet\'s try again, {name}!')
        return False
    return True


def get_game(game):
    greeting()
    name = welcome_user()
    print(game.DESCRIPTION)
    i = 1
    while i <= NUM_OF_ROUNDS:
        right_answer, question = game.get_question_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if comparison_responses(answer, right_answer, name) is False:
            break
        i += 1

        if i >= NUM_OF_ROUNDS + 1:
            return print(f"Congratulations, {name}!")
