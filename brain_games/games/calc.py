import operator
import random
# constants for the game
START_RANGE = 1
STOP_RANGE = 100
DESCRIPTION = 'What is the result of the expression?'


def get_result(first_number, second_number, oper):
    if oper == '+':
        result_of_calc = operator.add(first_number, second_number)
    elif oper == '-':
        result_of_calc = operator.sub(first_number, second_number)
    elif oper == '*':
        result_of_calc = operator.mul(first_number, second_number)
    else:
        return None

    return result_of_calc


def get_question_answer():
    # define random numbers
    first_number = random.randint(START_RANGE, STOP_RANGE)
    second_number = random.randint(START_RANGE, STOP_RANGE)
    # random operators are determined
    oper = random.choice(['+', '-', '*'])
    # ask a question
    question = f'{str(first_number)} {oper} {str(second_number)}'
    # getting the right answer
    right_answer = get_result(first_number, second_number, oper)

    return str(right_answer), question
