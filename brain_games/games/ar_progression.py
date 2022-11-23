
import random

from brain_games.games.constants import NUM_OF_ROUNDS, START_RANGE, STOP_RANGE
from brain_games.games.constants import MIN_ELEM, MAX_ELEM, FIRST_INDEX
from brain_games.games.constants import FIRST_NUM_STEP, SECOND_NUM_STEP
from brain_games.games.functions import welcome_user, question_for_user
from brain_games.games.functions import comparison_responses, answer_fo_user


def desc_game():
    print('What number is missing in the progression?')


def game():
    name = welcome_user()
    desc_game()
    i = 1
    while i <= NUM_OF_ROUNDS:
        right_answer, question = find_number()
        question_for_user(question)
        answer = answer_fo_user()
        if comparison_responses(answer, right_answer, name) is False:
            break
        i += 1

        if i >= NUM_OF_ROUNDS + 1:
            return print(f"Congratulations, {name}!")


def find_number():
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
