import random

DESCRIPTION='Answer "yes" if the number is even, otherwise answer "no".'

def generate_game():
    random_number = random.randint(1, 100)
    quest=str(random_number)
    answer_game= 'yes' if random_number % 2 == 0 else 'no'
    return quest, answer_game
