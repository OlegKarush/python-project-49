
import math
import random

from brain_games.games.constants import START_RANGE, STOP_RANGE


def desc_game():
    print('Find the greatest common divisor of given numbers.')


def get_question_answer():
    # определяются рандомные числа
    number_1 = random.randint(START_RANGE, STOP_RANGE)
    number_2 = random.randint(START_RANGE, STOP_RANGE)
    # получаем значение максимального общего делителя
    right_answer = math.gcd(number_1, number_2)
    question = f'{str(number_1)} {str(number_2)}'

    return right_answer, question
