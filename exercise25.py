# -*- coding: utf-8 -*-
"""
Practice Python Exercise 25

User picks a number between 1 and 100, program guesses it.

"""
# Wait function
import time
def wait(x):
    time.sleep(x)
    return

# Function for next guess
def nextguess(guess, hilo):
    global hilim
    global lolim
    if hilo >= 1:
        hilim = guess
    elif hilo <= -1:
        lolim = guess
    guess_next = guess - (hilo)*int((hilim - lolim)/2)
    return guess_next

# Intro
print("Let me try and guess your number!")
wait(1)
print("Pick a number between 1 and 100...")
wait(2)
print("Got it? I'll start guessing.")
wait(1.5)
print("Enter a positive number if my guess is too high,")
wait(1.5)
print("a negative number if my guess is too low,")
wait(1.5)
print("and 0 if my guess is right!")
wait(1.5)

# Play game
hilo = 2
lolim = 0
hilim = 100
guess = 50
count = 0
while hilo != 0:
    print("My guess is", guess, ". Is that...")
    count += 1
    hilo = int(input("..too high or too low: "))
    if hilo >= 1:
        hilo = 1
    elif hilo <= -1:
        hilo = -1
    guess = nextguess(guess, hilo)
print("Thanks for playing! I got your number in", count, "guesses.")
