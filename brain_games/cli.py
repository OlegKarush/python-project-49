#!/usr/bin/env python3
import prompt


def welcome_user():
    get_name = prompt.string("May I have your name? ")
    return print("Hello, " + get_name + "!")
