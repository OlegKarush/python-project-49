
import operator
import random

# констаны для игры
START_RANGE = 1
STOP_RANGE = 100
DESCRIPTION = 'What is the result of the expression?'


def get_question_answer():
    # определяются рандомные числа
    first_number = random.randint(START_RANGE, STOP_RANGE)
    second_number = random.randint(START_RANGE, STOP_RANGE)
    #  определяются рандомные опеаторы
    oper = random.choice(['+', '-', '*'])
    # Задается вопрос
    question = f'{str(first_number)} {oper} {str(second_number)}'
    # в зависимости от оператора получаем правильный ответ
    if oper == '+':
        right_answer = operator.add(first_number, second_number)
    elif oper == '-':
        right_answer = operator.sub(first_number, second_number)
    elif oper == '*':
        right_answer = operator.mul(first_number, second_number)

    return right_answer, question
