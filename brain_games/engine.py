import prompt

def engine_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count = 0
    print(game.DESCRIPTION)

    while count != 3:
        quest, answer_game=game.generate_game()
        print(f'Question: {quest}')
        answer = prompt.string('Your answer: ')
        if answer == answer_game:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{answer_game}'.")
            print(f"Let's try again, {name}!")
            break

    if count == 3:
        print(f"Congratulations, {name}!")
