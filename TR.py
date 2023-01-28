# rock paper scissors game code

import time
import random

with open('words.txt', 'r') as file:
    data = file.read()
    words = data.split()


def type_racer():

    def typetest():
        # This function records all the data while typing: time, accuracy etc.
        if start != '':
            print("Error")
        else:
            t0 = time.time()
            inputtext = str(input("Start typing: "))
            t1 = time.time()
            ''' Time ends when you finish typing and click enter'''
            timetaken = round(t1 - t0, 3)
            accuracy = len(set(inputtext.split()) & set(ranwords))
            accuracy = accuracy / wordcount * 100
            wpm = round((wordcount / timetaken) * 60, 2)
            print(f"Time: {timetaken} s Accuracy: {accuracy}% WPM: {wpm}")
    try:
        ''' Try/except block to filter out invalid inputs'''
        print('This is a typeracer game. Type as fast and accurately as you can. You will be asked for the amount of words you want to be tested on then you will be prompted to press enter to start, after you press enter you may being typing.')
        inputwordcount = int(input("How many words do you want to do? 50, 25, or 10: "))
    except ValueError:
        print("Error: Enter valid number")
        type_racer()

    if inputwordcount == 50:
        # 50 word settings
        ranwords = (random.sample(words, 50))
        print(*ranwords, sep=' ')
        wordcount = len(ranwords)
        start = str(input("Click Enter to Start"))
        typetest()
    elif inputwordcount == 25:
        # 25 word setting
        ranwords = (random.sample(words, 25))
        print(*ranwords, sep=' ')
        wordcount = len(ranwords)
        start = str(input("Click Enter to Start"))
        typetest()
    elif inputwordcount == 10:
        # 10 word setting
        ranwords = (random.sample(words, 10))
        print(*ranwords, sep=' ')
        wordcount = len(ranwords)
        start = str(input("Click Enter to Start"))
        typetest()
    else:
        print("Error: Enter valid number (50, 25, or 10)")
        type_racer()