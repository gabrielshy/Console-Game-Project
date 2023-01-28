# Francis Gabriel Anos
# Gaming Project - 3 Games:
# 1. Type Racer
# 2. Hangman
# 3. Rock Paper Scissors
# Skills used: Module knowledge, Try-Except, Boolean

import TR
import RPS
import HM


def restart_hm():
    retry_hm = input('Would you like to play again? y/n:  ')
    '''Created restart function'''
    if retry_hm == 'y':
        print("___________________________________________")
        HM.hangman()
        replay = True
    elif retry_hm == 'n':
        print("___________________________________________")
        menu()
        replay = False
    else:
        print('Invalid input')
        restart_hm()


def restart_rps():
    '''takes user input after win/lose round to return to menu or reset rps game'''
    retry = input('Would you like to play again? y/n:  ')
    if retry == 'y':
        print("___________________________________________")
        RPS.rps_game()
        replay = True
    elif retry == 'n':
        print("___________________________________________")
        menu()
        replay = False
    else:
        print('Invalid input')
        restart_rps()


def restart_tr():
    # Restart function
    retry_tr = input('Would you like to play again? y/n:  ')
    if retry_tr == 'y':
        print("___________________________________________")
        TR.type_racer()
        replay = True
    elif retry_tr == 'n':
        print("___________________________________________")
        menu()
        replay = False
    else:
        print('Invalid input')
        restart_tr()


def menu():
    replay = True
    option = input("Choose an option by typing the number of the game you want to play.\n"
                   "1. Type Racer\n"
                   "2. Hang Man\n"
                   "3. Rock Paper Scissors\n"
                   "Choose number: ")

    if option == '1':
        print("___________________________________________")
        TR.type_racer()
        restart_tr()
        while replay is True:
            restart_tr()
        if replay is False:
            menu()
    elif option == '2':
        print("___________________________________________")
        HM.hangman()
        restart_hm()
        while replay is True:
            restart_hm()
        if replay is False:
            menu()
    elif option == '3':
        print("___________________________________________")
        RPS.rps_game()
        restart_rps()
        while replay is True:
            restart_rps()
        if replay is False:
            menu()
    else:
        print("___________________________________________")
        print("Error: Invalid option")
        menu()


menu()
