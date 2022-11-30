
from brain_games.games.functions import welcome_user, question_for_user
from brain_games.games.functions import answer_fo_user, comparison_responses
from brain_games.games.constants import NUM_OF_ROUNDS


# the basic code of the games
def game(desc_game, get_question_answer):
    name = welcome_user()
    desc_game()
    i = 1
    while i <= NUM_OF_ROUNDS:
        right_answer, question = get_question_answer()
        question_for_user(question)
        answer = answer_fo_user()
        if comparison_responses(answer, right_answer, name) is False:
            break
        i += 1

        if i >= NUM_OF_ROUNDS + 1:
            return print(f"Congratulations, {name}!")
