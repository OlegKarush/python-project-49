import random
# constants for the game
START_RANGE = 1
STOP_RANGE = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    number_divisors = 0
    for item in range(2, number + 1):
        if (number % item) != 0:
            number_divisors += 0
        else:
            number_divisors += 1

    return number_divisors == 1


def get_question_answer():
    # define random number
    random_number = random.randint(START_RANGE, STOP_RANGE)
    # ask a question
    question = f'{random_number}'
    # getting the right answer
    if is_prime(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return str(right_answer), question
