import prompt
# constants for the game engine
NUM_OF_ROUNDS = 3


# game engine
def run_game(game):
    print('Welcome to the Brain Games!')
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
            print(
                f'\'{answer}\' is wrong answer ;(. '
                f'Correct answer was \'{right_answer}\'.'
                f'\nLet\'s try again, {name.capitalize()}!')
            return False
        i += 1

    print(f"Congratulations, {name.capitalize()}!")
