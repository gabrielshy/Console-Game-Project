# Hang Man game code

import random

with open('hangman_words.txt') as file:
    data = file.read()
    hang_words = data.split()


def hangman():

    '''Created special characters list in case the user inputs a special character on accident'''
    special_char = ['~', ':', "'", '+', '[', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    # Assignes variables
    secret_word = str(*(random.sample(hang_words, 1)))
    '''pulling a random word from the hangman_words.txt file'''
    print(f"The secret word has {len(secret_word)} characters")
    letters = []
    fail_count = 6
    test = True

    # function that lets user know how many letters there are left to guess
    def letters_left(x):
        letter_left = len(x)
        if letter_left != 0:
            print("There are", letter_left, "letters left")
        else:
            '''added restart when win'''
            print("You Win")

    # function that checks if the input is a letter
    def checker(guess):
        if guess in special_char:
            '''added special character check'''
            print("Error: please enter a letter")
            return True
        elif len(guess) > 1:
            '''added if there are more than 2 characters inputted check'''
            print("Error: please enter 1 letter")
            return True
        else:
            try:
                guess = int(guess)
                print("Error: please enter a letter")
                return True
            except:
                guess = str(guess)
                return False

    # creates a list for the secret word
    for i in range(len(secret_word)):
        letters.append(secret_word[i])
    print("You must guess all the letters in the secret word, if you fail six times you lose.")

    # gets and checks the input from the user
    while test == True:
        '''added '.lower()' to automatically turn the letter into lowercase in case they use capitalized letters'''
        guess = str(input("Enter a Letter: ")).lower()
        test = checker(guess)

    # decides if the guess given is correct and prompts them to guess again until they win or lose.
    while letters != [] and fail_count != 0:
        if guess in letters:
            letters.remove(guess)
            letters_left(letters)
            if secret_word == []:
                break
            guess = str(input('Good job, guess again! ')).lower()
            if checker(guess) == True:
                while checker(guess) == True:
                    guess = str(input("Enter a Letter: ")).lower()

        else:
            fail_count -= 1
            if fail_count != 6:
                print("Fail count is", (6 - fail_count))
            if fail_count == 0:
                '''added secret word reveal and restart when the player loses'''
                print(f"You lose, the word was '{secret_word}'")
                break
            guess = str(input('Wrong. Guess again: ')).lower()
            if checker(guess) == True:
                guess = str(input("Enter a Letter: ")).lower()
