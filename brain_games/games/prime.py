
import random

from brain_games.games.constants import START_RANGE, STOP_RANGE


def desc_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def get_question_answer():
    # определяется рандомное число
    random_number = random.randint(START_RANGE, STOP_RANGE)
    number_divisors = 0
    # создаем вопрос для печати
    question = f'{random_number}'
    # определяем числа для сравнения
    items = list(range(START_RANGE, random_number + 1))
    for item in items:
        if (random_number % item) != 0:
            number_divisors += 0
        else:
            number_divisors += 1
    if number_divisors == 2:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return right_answer, question
