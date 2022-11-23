
import prompt


def greeting():
    print('Welcome to the Brain Games!')


def welcome_user():
    get_name = prompt.string("May I have your name? ")
    print(f"Hello, {get_name.capitalize()}!")
    return get_name.capitalize()


def question_for_user(question):
    print(f'Question: {question}')


def answer_fo_user():
    answer = prompt.string('Your answer: ')
    return answer


def comparison_responses(answer, right_answer, name):
    if answer == str(right_answer):
        print("Correct!")
    else:
        print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{right_answer}'."
            f"\nLet's try again, {name}!")
        return False
    return True
