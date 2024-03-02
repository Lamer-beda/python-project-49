import random

DESCRIPTION='What is the result of the expression?'

def generate_game():
    operations = ['+', '-', '*']
    rand_operation = random.choice(operations)
    rand_num1 = random.randint(10, 50)
    rand_num2 = random.randint(1, 10)
    quest=f'{str(rand_num1)} {rand_operation} {str(rand_num2)}'
    match rand_operation:
        case '+':
            answer_game = str(rand_num1 + rand_num2)
        case '-':
            answer_game = str(rand_num1 - rand_num2)
        case '*':
            answer_game = str(rand_num1 * rand_num2)
    return quest, answer_game
