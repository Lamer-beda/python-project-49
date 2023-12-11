#!/usr/bin/env python3


import prompt
import random


def prime():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count != 3:
        random_number = random.randint(2, 20)
        print('Question: ' + str(random_number))
        answer = prompt.string('Your answer: ')
        if all(random_number % i != 0 for i in range(2, int(random_number ** 0.5) + 1)) == True and answer == 'yes':
            print('Correct!')
            count += 1
        elif all(random_number % i != 0 for i in range(2, int(random_number ** 0.5) + 1)) != True and answer == 'no':
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\n" +
                       f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


def main():
    print('Welcome to the Brain Games!')
    prime()


if __name__ == '__main__':
    main()