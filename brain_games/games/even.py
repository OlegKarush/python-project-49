import random
# constants for the game
START_RANGE = 1
STOP_RANGE = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_answer():
    # define random number
    random_number = random.randint(START_RANGE, STOP_RANGE)
    # ask a question
    question = f'{random_number}'
    # check the number is even
    # getting the right answer
    if is_even(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return str(right_answer), question
