import random
import math

DESCRIPTION="Find the greatest common divisor of given numbers."

def generate_game():
    rand_num1 = random.randint(1, 50)
    rand_num2 = random.randint(1, 100)
    quest=f'{rand_num1} {rand_num2}'
    while rand_num2 != 0:
        rand_num1, rand_num2 = rand_num2, rand_num1 % rand_num2
    answer_game=str(math.gcd(rand_num1, rand_num2))
    return quest, answer_game
