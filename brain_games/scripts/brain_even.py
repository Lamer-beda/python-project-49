#!/usr/bin/env python3


import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


def numbers():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    #right = prompt.string('Your answer:')
    #if right == 

def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    numbers()


if __name__ == '__main__':
    main()

