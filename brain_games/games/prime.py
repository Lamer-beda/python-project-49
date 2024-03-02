import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_game():
    quest = random.randint(2, 20)
    game = all(quest % i != 0 for i in range(2, int(quest ** 0.5) + 1))
    answer_game = 'yes' if game is True else 'no'
    return quest, answer_game
