
import random

from brain_games.games.constants import START_RANGE, STOP_RANGE


# описание игры
def desc_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def get_question_answer():
    # выбираем рандомное число
    random_number = random.randint(START_RANGE, STOP_RANGE)
    question = f'{random_number}'

    # определяем четность числа
    if random_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return right_answer, question
