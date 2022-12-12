#!/usr/bin/env python3

import prompt

from brain_games.engine import GREETING


def main():
    print(GREETING)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name.capitalize()}!')


if __name__ == '__main__':
    main()
