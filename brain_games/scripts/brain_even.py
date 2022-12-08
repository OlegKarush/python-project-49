#!/usr/bin/env python3

from brain_games.engine import get_game
from brain_games.games import even


def main():
    get_game(even)


if __name__ == '__main__':
    main()
