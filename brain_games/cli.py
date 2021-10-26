#!/usr/bin/env python

import prompt


def welcome_user():
    # User should enter a name

    name = prompt.string('May I have your name? ')
    print('Hello, ', name, '!')
