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


def get_progression(start_progress, step_progress):
    num_elem = random.randint(MIN_ELEM, MAX_ELEM)
    ind_hidden_num = random.randint(FIRST_INDEX, num_elem - 1)
    num = start_progress
    list_progress = []
    i = 1
    # creating a list
    while i <= num_elem:
        list_progress.append(num)
        num = num + step_progress
        i += 1
    # getting the right answer
    right_answer = list_progress[ind_hidden_num]
    # replacing one random element with ".."
    list_progress[ind_hidden_num] = ('..')

    return list_progress, right_answer


def get_question_answer():
    # define random numbers
    start_progress = random.randint(START_RANGE, STOP_RANGE)
    step_progress = random.randint(FIRST_NUM_STEP, SECOND_NUM_STEP)
    list_progress, right_answer = get_progression(start_progress, step_progress)
    # ask a question
    question = (" ".join(map(str, list_progress)))

    return str(right_answer), question
