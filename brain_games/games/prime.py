
import random

from brain_games.games.constants import num_of_rounds, start_range, stop_range
from brain_games.games.functions import welcome_user, question_for_user
from brain_games.games.functions import comparison_responses, answer_fo_user


def desc_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def game():
    name = welcome_user()
    desc_game()
    i = 1

    while i <= num_of_rounds:
        right_answer, question = is_prime()
        question_for_user(question)
        answer = answer_fo_user()
        if comparison_responses(answer, right_answer, name) is False:
            break
        i += 1

        if i >= num_of_rounds + 1:
            return print(f"Congratulations, {name}!")


def is_prime():
    # определяется рандомное число
    random_number = random.randint(start_range, stop_range)
    number_divisors = 0
    # создаем вопрос для печати
    question = f'{random_number}'
    # определяем числа для сравнения
    items = list(range(start_range, random_number + 1))
    for item in items:
        if (random_number % item) != 0:
            number_divisors += 0
        else:
            number_divisors += 1
    if number_divisors == 2:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return right_answer, question
