# -*- coding: utf-8 -*-
"""
Practice Python Exercise 31

Hangman

"""
# Function to display game
def display(board):
    for letter in board:
        print(letter, end = " ")
        
def board():
    board = []
    for i in range(0,len(word)):
        board.append('_ ')
    for i in range(0,len(word)):
        for letter in guesses:
            if letter == word[i]:
                board[i] = letter
    return(board)

def check(board):
    current = ''
    for letter in board:
        if letter.isalpha():
            current += letter
    return current
    
# Generate word to guess
dictionary = []
filename = "SOWPODS.txt"
with open(filename, 'r') as open_file:
    for line in open_file:
        line = line.strip()
        dictionary.append(line)       
import random
index = random.randint(1,len(dictionary))
word = str(dictionary[index])

# Play game
count = 0
guesses = []
print("Welcome to Hangman!")
while count < 6:
    display(board())
    guess = str(input("Guess a letter:"))
    guess = guess.upper()
    if guess in guesses:
        print("You already guessed that!")
    elif guess not in word:
        print("Incorrect!")
        count += 1
    elif guess in word:
        print("Correct!")
    guesses.append(guess)
    if check(board()) == word:
        print(word)
        print("You win!")
        break
if check(board()) != word:
    print("You lose!")
    print("The word was: ", word)