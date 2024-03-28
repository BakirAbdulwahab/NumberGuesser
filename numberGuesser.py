#########################################################################
# Date Created: 03/28/2024                                              #
# Name of Project: Number Guesser                                       #
# Conceptes Used: If/Else conditions, Variables, Data Types, Operators, #
#                 While loops, Elif condition.                          #
#########################################################################

import random

print("------------------------------------")
print("Welcome to the Number Guessing Game!")
print("------------------------------------")

maxNumber = int(input("\nType the maximum number to guess: "))

randomNumber = random.randint(0, maxNumber)

guesses = 0

if maxNumber <= 0:
    print("\nYou can't choose a number below 1. Please try again!\n")
else:
    print("\nOkay, let's start guessing!\n")

    while True:
        guesses += 1
        userGuess = int(input("Make a guess: "))

        if userGuess == randomNumber:
            print("\nYou got it correct!\n")
            break
        elif userGuess < randomNumber:
            print("\nYour guess is lower than the number. Guess higher!\n")
            continue
        elif userGuess > randomNumber:
            print("\nYour guess is higher than the number. Guess lower!\n")
            continue
        else:
            print("\nYou got it incorrect!\n")
            continue

if guesses < 2:
    print(f"Okay! You got it in {guesses} guess!")
else:
    print(f"Okay! You got it in {guesses} guesses!")

print("\n\nThanks for Playing!!\n\n")
