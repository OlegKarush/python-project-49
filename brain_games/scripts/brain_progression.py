#!/usr/bin/env python3

from brain_games.games.functions import greeting
from brain_games.scripts.engine import game
from brain_games.games.ar_progression import get_question_answer, desc_game


def main():
    greeting()
    game(desc_game, get_question_answer)


if __name__ == '__main__':
    main()
