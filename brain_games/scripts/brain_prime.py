#!/usr/bin/env python3


import prompt
import random


def prime():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count != 3:
        quest = random.randint(2, 20)
        print('Question: ' + str(quest))
        answer = prompt.string('Your answer: ')
        game = all(quest % i != 0 for i in range(2, int(quest ** 0.5) + 1))
        if game is True and answer == 'yes':
            print('Correct!')
            count += 1
        elif game is not True and answer == 'no':
            print('Correct!')
            count += 1
        elif game is not True and answer == 'yes':
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print("Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print("'no' is wrong answer ;(.", end=' ')
            print("Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


def main():
    print('Welcome to the Brain Games!')
    prime()


if __name__ == '__main__':
    main()
