#!/usr/bin/env python3

import prompt
from random import randint


def determine_even_number():
    i = 3
    
    while i > 0:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and answer.lower() == 'yes':
            print('Correct!')
        elif random_number % 2 != 0 and answer.lower() == 'no':
            print('Correct!')
        else:
            return print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, ,,!")
        i -= 1
        
    return print(f"Congratulations, bb!")
