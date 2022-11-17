#!/usr/bin/env python3

import prompt

number_of_rounds = 3
beginning_range = 1
stop_range = 100
min_elem = 5
max_elem = 10
first_index = 0
first_num_step = -100
second_num_step = 100


def welcome_user():
    get_name = prompt.string("May I have your name? ")
    print(f"Hello, {get_name.capitalize()}!")
    return get_name.capitalize()


def question_for_user():
    answer = prompt.string('Your answer: ')
    return answer


def comparison_responses(answer_user, right_answer, name):
    if answer_user == right_answer:
        print("Correct!")
    else:
        print(
            f"'{answer_user}' is wrong answer ;(. "
            f"Correct answer was '{right_answer}'."
            f"\nLet's try again, {name}!")
        return False
    return True
