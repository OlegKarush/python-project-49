import math
import random
# constants for the game
START_RANGE = 1
STOP_RANGE = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_answer():
    # define random numbers
    number_1 = random.randint(START_RANGE, STOP_RANGE)
    number_2 = random.randint(START_RANGE, STOP_RANGE)
    # get the value of the maximum common divisor
    # getting the right answer
    right_answer = math.gcd(number_1, number_2)
    # ask a question
    question = f'{str(number_1)} {str(number_2)}'

    return str(right_answer), question
