#!/usr/bin/env python3


import prompt
import random


def numbers():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count != 3:
        random_number = random.randint(1, 100)
        print('Question: ' + str(random_number))
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
            count += 1
        elif random_number % 2 != 0 and answer == 'no':
            print('Correct!')
            count += 1
        else:
            if answer == 'yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'.\n
                        Let's try again," + name + "!")
                break
            else:
                 print("'no' is wrong answer ;(. Correct answer was 'yes'.\n
                         Let's try again," + name + "!")
                 break
    if count == 3:
        print('Congratulations,' + name + '!')


def main():
    print('Welcome to the Brain Games!')
    numbers()


if __name__ == '__main__':
    main()
