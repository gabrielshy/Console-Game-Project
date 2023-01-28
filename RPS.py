# Rock Paper Scissors game code

from random import randrange


def rps_game():
    '''Rock paper scissors game where user types in their move against a randomly generated move'''
    try:
        rps = randrange(1, 4)
        print('This is a game of Rock, Paper, or Scissors.')
        user_input = input(str('Please type rock, paper, or scissors(in all lowercase): ')).lower()
    except:
        print('Invalid input. Please retry.')
        user_input = input('Please type rock, paper, or scissors(in all lowercase): ').lower()

    while user_input != 'exit':

        if user_input == 'rock':
            if rps == 1:
                print("Rock!\nIt's a tie! Try Again. ")
                user_input = input('Please type rock, paper, or scissors(in all lowercase): ').lower()
                rps = randrange(1, 4)
                continue
            elif rps == 2:
                print('Scissors\nYou win!')
                user_input = 'exit'
            elif rps == 3:
                print('Paper\nYou lose!')
                user_input = 'exit'

        elif user_input == 'paper':
            if rps == 1:
                print("Rock!\nYou win! ")
                user_input = 'exit'
                break
            elif rps == 2:
                print('Scissors\nYou lose!')
                user_input = 'exit'
                break
            elif rps == 3:
                print("Paper\nIt's a tie! Try again.")
                user_input = input('Please type rock, paper, or scissors(in all lowercase): ').lower()
                rps = randrange(1, 4)
                continue

        elif user_input == 'scissors':
            if rps == 1:
                print("Rock!\nYou lose! ")
                user_input = 'exit'
                break
            elif rps == 2:
                print("Scissors\nIt's a tie! Try again.")
                user_input = input('Please type rock, paper, or scissors(in all lowercase): ').lower()
                rps = randrange(1, 4)
                continue
            elif rps == 3:
                print("Paper\nYou win!")
                user_input = 'exit'
                break
        else:
            print('Invalid input. Try again')
            user_input = input('Please type rock, paper, or scissors(in all lowercase): ').lower()