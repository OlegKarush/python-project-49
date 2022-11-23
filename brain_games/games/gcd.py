
import math
import random

from brain_games.games.constants import NUM_OF_ROUNDS, START_RANGE, STOP_RANGE
from brain_games.games.functions import welcome_user, question_for_user
from brain_games.games.functions import comparison_responses, answer_fo_user


def desc_game():
    print('Find the greatest common divisor of given numbers.')


def game():
    name = welcome_user()
    desc_game()
    i = 1
    while i <= NUM_OF_ROUNDS:
        right_answer, question = find_divisor()
        question_for_user(question)
        answer = answer_fo_user()
        if comparison_responses(answer, right_answer, name) is False:
            break
        i += 1

        if i >= NUM_OF_ROUNDS + 1:
            return print(f"Congratulations, {name}!")


def find_divisor():
    # определяются рандомные числа
    number_1 = random.randint(START_RANGE, STOP_RANGE)
    number_2 = random.randint(START_RANGE, STOP_RANGE)
    # получаем значение максимального общего делителя
    right_answer = math.gcd(number_1, number_2)
    question = f'{str(number_1)} {str(number_2)}'

    return right_answer, question
