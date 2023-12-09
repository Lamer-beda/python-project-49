#!/usr/bin/env python3


import prompt
import random

def calculator():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count = 0
    operations=['+', '-', '*']
    random_operation = random.choice(operations)
    print('What is the result of the expression?')
    while count != 3:
        operations=['+', '-', '*']
        random_operation = random.choice(operations)
        rand_num_1=random.randint(10,50)
        rand_num_2=random.randint(1,10)
        print('Question: ' + str(rand_num_1) + random_operation + str(rand_num_2))
        answer = prompt.string('Your answer: ')
        if random_operation == '+':
            if rand_num_1 + rand_num_2 == int(answer):
                print('Correct!')
                count +=1
            else:
                print ("'" + answer + "' is wrong answer ;(. Correct answer was '" + str(rand_num_1 + rand_num_2) + "'\nLet's try again, "+name+"!")
                break
        if random_operation == '-':
            if rand_num_1 - rand_num_2 == int(answer):
                print('Correct!')
                count +=1
            else:
                print ("'" + answer + "' is wrong answer ;(. Correct answer was '" + str(rand_num_1 - rand_num_2) + "'\nLet's try again, "+name+"!")
                break
        if random_operation =='*':
            if rand_num_1 * rand_num_2 == int(answer):
                print('Correct!')
                count +=1
            else:
                print ("'" + answer + "' is wrong answer ;(. Correct answer was '" + str(rand_num_1 * rand_num_2) + "'\nLet's try again, "+name+"!")
                break
    if count ==3:
            print('Congratulations, ' + name + '!')



def main():
    print('Welcome to the Brain Games!')
    calculator()


if __name__ == '__main__':
    main()

#
