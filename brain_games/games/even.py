
import random

# констаны для игры
START_RANGE = 1
STOP_RANGE = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_answer():
    # выбираем рандомное число
    random_number = random.randint(START_RANGE, STOP_RANGE)
    question = f'{random_number}'

    # определяем четность числа
    if is_even(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return right_answer, question
