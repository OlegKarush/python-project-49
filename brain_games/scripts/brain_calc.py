#!/usr/bin/env python3

from brain_games.games.calc import get_math
from brain_games.cli import welcome_user, question_for_user
from brain_games.cli import comparison_responses, number_of_rounds


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    i = 1

    while i <= number_of_rounds:
        right_answer = get_math()
        answer_user = question_for_user()
        if comparison_responses(answer_user, right_answer, name) is False:
            break
        i += 1

        if i >= number_of_rounds + 1:
            return print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
