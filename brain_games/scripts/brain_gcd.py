#!/usr/bin/env python3


import prompt
import random


def gcd():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count = 0
    print("Find the greatest common divisor of given numbers.")
    while count != 3:
        rand_num1 = random.randint(1, 50)
        rand_num2 = random.randint(1, 100)
        print(f"Question: {str(rand_num1)} {str(rand_num2)}")
        answer = prompt.string('Your answer: ')
        while rand_num2 != 0:
            rand_num1, rand_num2 = rand_num2, rand_num1 % rand_num2
        if str(rand_num1) == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{rand_num1}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")


def main():
    print('Welcome to the Brain Games!')
    gcd()


if __name__ == '__main__':
    main()
