
import random

from brain_games.games.constants import num_of_rounds, start_range, stop_range
from brain_games.games.constants import min_elem, max_elem, first_index
from brain_games.games.constants import first_num_step, second_num_step
from brain_games.games.functions import welcome_user, question_for_user
from brain_games.games.functions import comparison_responses, answer_fo_user


def desc_game():
    print('What number is missing in the progression?')


def game():
    name = welcome_user()
    desc_game()
    i = 1
    while i <= num_of_rounds:
        right_answer, question = find_number()
        question_for_user(question)
        answer = answer_fo_user()
        if comparison_responses(answer, right_answer, name) is False:
            break
        i += 1

        if i >= num_of_rounds + 1:
            return print(f"Congratulations, {name}!")


def find_number():
    # определяем рандомные числа
    number_elements = random.randint(min_elem, max_elem)
    index_hidden_number = random.randint(first_index, number_elements - 1)
    start_progression = random.randint(start_range, stop_range)
    step_progression = random.randint(first_num_step, second_num_step)
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
