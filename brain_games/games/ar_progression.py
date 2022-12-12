
import random

# constants for the game
START_RANGE = 1
STOP_RANGE = 100
MIN_ELEM = 5
MAX_ELEM = 10
FIRST_INDEX = 0
FIRST_NUM_STEP = -100
SECOND_NUM_STEP = 100
DESCRIPTION = 'What number is missing in the progression?'


def get_question_answer():
    # define random numbers
    number_elements = random.randint(MIN_ELEM, MAX_ELEM)
    index_hidden_number = random.randint(FIRST_INDEX, number_elements - 1)
    start_progression = random.randint(START_RANGE, STOP_RANGE)
    step_progression = random.randint(FIRST_NUM_STEP, SECOND_NUM_STEP)
    i = 1
    num = start_progression
    list_progress = []

    # creating a list
    while i <= number_elements:
        list_progress.append(num)
        num = num + step_progression
        i += 1

    # getting the right answer
    right_answer = list_progress[index_hidden_number]
    # replacing one random element with ".."
    list_progress[index_hidden_number] = ('..')
    # ask a question
    question = (" ".join(map(str, list_progress)))

    return str(right_answer), question
