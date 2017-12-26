# -*- coding: utf-8 -*-
"""
Practice Python Exercise 9

Generate a random number in a range. Have user guess the number and tell them
if their guess was too high, too low, or right. Track the number of guesses

"""

# Define functions
def get_number(x):
    guess = int(input("Guess number %s. Enter:" % x))
    return guess

import time
def wait(x):
    time.sleep(x)
    return

# Initiate game
print("Welcome to Guess-the-Number!")
wait(.5)
guess_range = int(input("Guess numbers between 1 and:"))
tracker = 1
import random
ans = random.randint(1, guess_range)
holder = 0

# Play game
while holder!= ans:
    if (tracker-1) % 5 == 0:
        print("Type a letter to quit")
        wait(1)
    holder = get_number(tracker)
    if holder == ans:
        print("You won in %d guesses!" % tracker)
        break
    elif holder < ans:
        print("Too low, guess again!")
    elif holder > ans:
        print("Too high, guess again!")
    tracker += 1