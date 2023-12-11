#!/usr/bin/env python3


import prompt
import random


def calcul():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count = 0
    print('What is the result of the expression?')
    while count != 3:
        operations = ['+', '-', '*']
        rand_operation = random.choice(operations)
        rand_num1 = random.randint(10, 50)
        rand_num2 = random.randint(1, 10)
        print(f"Question: {str(rand_num1)} {rand_operation} {str(rand_num2)}")
        answer = prompt.string('Your answer: ')
        match rand_operation:
            case '+':
                if rand_num1 + rand_num2 == int(answer):
                    print('Correct!')
                    count += 1
                else:
                    print(f"'{answer}' is wrong answer ;(.", end=' ')
                    print(f"Correct answer was '{str(rand_num1 + rand_num2)}'.")
                    print(f"Let's try again, {name}!")
                    break
            case '-':
                if rand_num1 - rand_num2 == int(answer):
                    print('Correct!')
                    count += 1
                else:
                    print(f"'{answer}' is wrong answer ;(.", end=' ')
                    print(f"Correct answer was '{str(rand_num1 - rand_num2)}'.")
                    print(f"Let's try again, {name}!")
                    break
            case '*':
                if rand_num1 * rand_num2 == int(answer):
                    print('Correct!')
                    count += 1
                else:
                    print(f"'{answer}' is wrong answer ;(.", end=' ')
                    print(f"Correct answer was '{str(rand_num1 * rand_num2)}'.")
                    print(f"Let's try again, {name}!")
                    break
    if count == 3:
        print(f"Congratulations, {name}!")


def main():
    print('Welcome to the Brain Games!')
    calcul()


if __name__ == '__main__':
    main()
