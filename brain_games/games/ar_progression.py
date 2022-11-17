#!/usr/bin/env python3

import random
from brain_games.cli import beginning_range, stop_range, min_elem, max_elem
from brain_games.cli import first_index, first_num_step , second_num_step


def find_number():
    number_elements = random.randint(min_elem, max_elem)
    index_hidden_number = random.randint(first_index, number_elements - 1)
    start_progression = random.randint(beginning_range, stop_range)
    step_progression = random.randint(first_num_step, second_num_step)
    i = 1
    num = start_progression
    list_progress = []
    while i <= number_elements:
        num = num + step_progression
        list_progress.append(num)
        i += 1

    right_answer = list_progress[index_hidden_number]
    list_progress[index_hidden_number] = ('..')
    # печать вопроса + список элементов прогрессии
    print('Question:', end=' ')
    for num in list_progress:
        print(num, end=' ')
    print('')

    return str(right_answer)
