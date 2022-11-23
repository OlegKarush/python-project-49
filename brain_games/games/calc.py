
import operator
import random

from brain_games.games.constants import num_of_rounds, start_range, stop_range
from brain_games.games.functions import welcome_user, question_for_user
from brain_games.games.functions import comparison_responses, answer_fo_user


def desc_game():
    print('What is the result of the expression?')


def game():
    name = welcome_user()
    desc_game()
    i = 1
    while i <= num_of_rounds:
        right_answer, question = get_math()
        question_for_user(question)
        answer = answer_fo_user()
        if comparison_responses(answer, right_answer, name) is False:
            break
        i += 1

        if i >= num_of_rounds + 1:
            return print(f"Congratulations, {name}!")


def get_math():
    i = 1

    while i <= num_of_rounds:
        # определяются рандомные числа
        first_number = random.randint(start_range, stop_range)
        second_number = random.randint(start_range, stop_range)
        #  определяются рандомные опеаторы
        oper = random.choice(["+", "-", "*"])
        # Задается вопрос
        question = f'{str(first_number)} {oper} {str(second_number)}'
        # в зависимости от оператора получаем правильный ответ
        if oper == "+":
            right_answer = operator.add(first_number, second_number)
        elif oper == "-":
            right_answer = operator.sub(first_number, second_number)
        elif oper == "*":
            right_answer = operator.mul(first_number, second_number)
        i += 1

    return right_answer, question
