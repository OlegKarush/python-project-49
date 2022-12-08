
import random

# констаны для игры
START_RANGE = 1
STOP_RANGE = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    number_divisors = 0
    for item in range(START_RANGE, number + 1):
        if (number % item) != 0:
            number_divisors += 0
        else:
            number_divisors += 1

    return number_divisors == 2


def get_question_answer():
    # определяется рандомное число
    random_number = random.randint(START_RANGE, STOP_RANGE)
    # создаем вопрос
    question = f'{random_number}'

    if is_prime(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return right_answer, question
