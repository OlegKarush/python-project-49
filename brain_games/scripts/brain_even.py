#!/usr/bin/env python3
import brain_games
#from brain_games import main
from brain_games.even import determine_even_number


def main():
    brain_games.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    determine_even_number()


if __name__ == '__main__':
    main()
