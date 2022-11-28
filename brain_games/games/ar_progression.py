
import random

from brain_games.games.constants import START_RANGE, STOP_RANGE
from brain_games.games.constants import MIN_ELEM, MAX_ELEM, FIRST_INDEX
from brain_games.games.constants import FIRST_NUM_STEP, SECOND_NUM_STEP


def desc_game():
    print('What number is missing in the progression?')


def get_question_answer():
    # определяем рандомные числа
    number_elements = random.randint(MIN_ELEM, MAX_ELEM)
    index_hidden_number = random.randint(FIRST_INDEX, number_elements - 1)
    start_progression = random.randint(START_RANGE, STOP_RANGE)
    step_progression = random.randint(FIRST_NUM_STEP, SECOND_NUM_STEP)
    i = 1
    num = start_progression
    list_progress = []

    # создаем список
    while i <= number_elements:
        list_progress.append(num)
        num = num + step_progression
        i += 1

    # заменяем один рандомный элемент на ".."
    right_answer = list_progress[index_hidden_number]
    list_progress[index_hidden_number] = ('..')
    # создаем список элеменов для печати
    list_2 = ""
    for num in list_progress:
        list_2 = list_2 + str(num) + " "
    question = list_2

    return right_answer, question
