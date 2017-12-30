# -*- coding: utf-8 -*-
"""
Practice Python Exercise 18

Cows and Bulls game.

Ask user for a four digit number. For every correct digit in correct location,
they get a cow. For every correct digit in incorrect location, they get a bull.
Tell them how many cows and bulls they got each round. When they guess the
number, the game is over.

"""
# Use my wait function to smooth user interface
import time
def wait(x):
    time.sleep(x)
    return

# Function for guesses
def get_guess():
    guess = str(input("Enter your guess: "))
    while len(guess) != 4:
        print("Guesses must be four digits.")
        wait(1)
        guess = str(input("Enter your guess: "))
    return guess

# Function for getting cows and bulls
def cowsbulls(guess):
    cowsbulls = [0, 0]
    for i in range(0,4):
        if guess[i] == ans[i]:
            cowsbulls[0] += 1
        elif ans[i] == guess[(i+1)%4] or ans[i] == guess[(i+2)%4] or ans[i] == guess[(i+3)%4]:
            cowsbulls[1] += 1
    return cowsbulls


# Introduce Cows and Bulls
print("Welcome to Cows and Bulls! (To quit, type 'quit')")
wait(1)
print("Guess a four digit number. For each correct digit in the correct place, you get a cow.")
wait(2)
print("For each correct digit out of place, you get a bull. Guess until you get the number!")
wait(2)

# Play game
import random
ans = str(random.randint(0000,9999))
# For testing
# print(ans)
turns = 0
guess = 0
while guess != ans:
    guess = get_guess()
    if guess == "quit":
        print("You lose! The answer was", ans, ".")
        break
    cowsbulls = cowsbulls(guess)
    print("%s has %d cows and %d bulls." % (guess, cowsbulls[0], cowsbulls[1]))
    turns += 1
if guess == ans:
    print("Congrats, you got the answer", ans, "in", turns, "guesses!")