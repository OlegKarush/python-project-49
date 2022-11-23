
import random

from brain_games.games.constants import num_of_rounds, start_range, stop_range
from brain_games.games.functions import welcome_user, question_for_user
from brain_games.games.functions import comparison_responses, answer_fo_user

# описание игры
def desc_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def game():
    name = welcome_user()
    desc_game()
    i = 1
    while i <= num_of_rounds:
        right_answer, question = specify_even()
        question_for_user(question)
        answer = answer_fo_user()
        if comparison_responses(answer, right_answer, name) is False:
            break
        i += 1

        if i >= num_of_rounds + 1:
            return print(f"Congratulations, {name}!")

    return right_answer, question


def specify_even():
    # выбираем рандомное число
    random_number = random.randint(start_range, stop_range)
    question = f'{random_number}'

    # определяем четность числа
    if random_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return right_answer, question
