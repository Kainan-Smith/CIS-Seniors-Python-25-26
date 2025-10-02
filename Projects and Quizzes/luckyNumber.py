'''
File: luckyNumber.py
Author: Kainan Smith
Class: CIS Seniors
Date: 10/2/25
'''

import random

# Game statistics
total_rounds = 0
total_wins = 0
total_guesses = 0

print("=" * 50)
print("  WELCOME TO THE LUCKY NUMBER GUESSING GAME!")
print("=" * 50)
print()

randomNumber = random.randint(1, 50)
maxAttempts = 7
attempts = 0
gameDone = False
rounds = 1

print("I'm thinking of a lucky number between 1 and 50...")
print(f"You have {maxAttempts} attempts to guess it!")

# Main game loop - play multiple rounds
while attempts < maxAttempts:
    print(f"\nRound {rounds}:")
    while gameDone == False:
        if attempts > 7 and guess != randomNumber:
            print("\n\nSorry, but you failed...\nBetter luck next time!")
            gameDone = True
        guess = int(input(f"Enter guess number {attempts + 1}: "))
        if guess > 50 or guess < 1:
            print("Invalid number, please enter a number between 1 and 50.")
            attempts -= 1
        elif guess == randomNumber:
            print("Conglomeration!")
            print(f"It took you {attempts} guesses!")
            gameDone = True
        else:
            print("Not quite!")
            if guess < randomNumber:
                print("Too low!\n")
            elif guess > randomNumber:
                print("Too high!\n") 
        attempts += 1
        if gameDone == True:
            playAgain = input("Do you want to play again? ")
            if playAgain == "no":
                break
            else:
                attempts = 0
                rounds += 1
    break

# Display final statistics
# TODO: Show total rounds, wins, and average guesses per round

print("\nThanks for playing! Goodbye!")