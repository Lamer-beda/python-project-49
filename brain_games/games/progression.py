import random

DESCRIPTION='What number is missing in the progression?'

def generate_game():
    l_prog = random.randint(5, 10)
    f_elem = random.randint(1, 50)
    diff = random.randint(1, 10)
    progression = [f_elem + (i - 1) * diff for i in range(1, l_prog + 1)]
    index = random.randint(0, len(progression) - 1)
    answer_game = progression[index]
    progression[index] = '..'
    quest=' '.join(map(str, progression))
    return quest, answer_game
