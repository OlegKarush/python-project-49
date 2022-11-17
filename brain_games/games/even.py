#!/usr/bin/env python3

import random
from brain_games.cli import beginning_range, stop_range


def specify_even():
    random_number = random.randint(beginning_range, stop_range)
    print(f'Question: {random_number}')

    if random_number % 2 == 0:
        right_answer = 'yes'
    elif random_number % 2 != 0:
        right_answer = 'no'

    return right_answer
