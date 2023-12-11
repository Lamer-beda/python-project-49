#!/usr/bin/env python3


import prompt
import random


def progress():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count = 0
    print('What number is missing in the progression?')
    while count != 3:
        l_prog = random.randint(5, 10)
        f_elem = random.randint(1, 50)
        diff = random.randint(1, 10)
        progression = [f_elem + (i - 1) * diff for i in range(1, l_prog + 1)]
        index = random.randint(0, len(progression) - 1)
        answer_game = progression[index]
        progression[index] = '..'
        print("Question: ", end='')
        for num in progression:
            print(num, end=' ')
        answer = prompt.string('\nYour answer: ')
        if answer_game == int(answer):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{answer_game}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")


def main():
    print('Welcome to the Brain Games!')
    progress()


if __name__ == '__main__':
    main()
