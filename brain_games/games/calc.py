#!/usr/bin/env python3

import operator
import prompt
import random
from brain_games.cli import welcome_user


def solving_expression():
    i = 3
    name = welcome_user()
    print('What is the result of the expression?')

    # цикл ограничивает количество вопросов = 3
    while i > 0:
        # определяются рандомные числа
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        #  определяются рандомные опеаторы
        oper = random.choice(["+", "-", "*"])
        # Задается вопрос, ввод ответа
        print(f'Question: {str(number_1)} {oper} {str(number_2)}')
        answer = prompt.string('Your answer: ')

        # в зависимости от оператора, производится мат.операция и сравниваются ответы
        if answer[0] != '-' and answer.isnumeric():
            if oper == "+":
                result = operator.add(number_1, number_2)
                if int(answer) != result:
                    return print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
                print("Correct!")
            elif oper == "-":
                result = operator.sub(number_1, number_2)
                if int(answer) != result:
                    return print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
                print("Correct!")
            elif oper == "*":
                result = operator.mul(number_1, number_2)
                if int(answer) != result:
                    return print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
                print("Correct!")
        # проверям на: наличие знака "-", циферность
        elif answer[0] == '-' and answer[1:].isnumeric():
            result = operator.sub(number_1, number_2)
            if int(answer) != result:
                return print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
            print("Correct!")
        else:
            return print(f"'{answer}' is wrong answer ;(. You need to enter the numbers!\nLet's try again, {name}!")

        i -= 1

    return print(f"Congratulations, {name}!")
