#!/usr/bin/env python3


def welcome_user():
    import prompt
    get_name = prompt.string("May I have your name? ")
    return print("Hello, " + get_name + "!")
welcome_user()