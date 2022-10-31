#!/usr/bin/env python3

import prompt
from random import randint
from brain_games.cli import welcome_user


def determine_even_number():
    i = 3
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    while i > 0:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and answer.lower() == 'yes':
            print('Correct!')
        elif random_number % 2 != 0 and answer.lower() == 'no':
            print('Correct!')
        else:
            return print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
        i -= 1

    return print(f"Congratulations, {name}!")
