#!/usr/bin/env python3

import prompt


def welcome_user():
    get_name = prompt.string("May I have your name? ")
    print(f"Hello, {get_name.capitalize()}!")
    return get_name.capitalize()
