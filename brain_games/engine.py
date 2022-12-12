
import prompt

# constants for the game engine
NUM_OF_ROUNDS = 3
GREETING = 'Welcome to the Brain Games!'


# game engine
def run_game(game):
    print(GREETING)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name.capitalize()}!')
    print(game.DESCRIPTION)
    i = 1
    while i <= NUM_OF_ROUNDS:
        right_answer, question = game.get_question_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == right_answer:
            print('Correct!')
        else:
            return print(
                f'\'{answer}\' is wrong answer ;(. '
                f'Correct answer was \'{right_answer}\'.'
                f'\nLet\'s try again, {name.capitalize()}!')
        i += 1

        if i > NUM_OF_ROUNDS:
            return print(f"Congratulations, {name.capitalize()}!")
