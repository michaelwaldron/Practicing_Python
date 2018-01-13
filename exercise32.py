# -*- coding: utf-8 -*-
"""
Practice Python Exercise 32

Hangman - with drawn man

"""
# Display game
def display(board):
    for letter in board:
        print(letter, end = " ")        
def board(word, guesses):
    board = []
    for i in range(0,len(word)):
        board.append('_ ')
    for i in range(0,len(word)):
        for letter in guesses:
            if letter == word[i]:
                board[i] = letter
    return(board)

# Check game
def check(board):
    current = ''
    for letter in board:
        if letter.isalpha():
            current += letter
    return current

# Print man
def man(count):
    if count == 0:
        print('    ___ ')    
        print('   |    ')
        print('   |    ')
        print("___|     ")
    elif count == 1:
        print('    ___ ')    
        print('   |  O ')
        print('   |   ')
        print("___|     ")
    elif count == 2:
        print('    ___ ')    
        print('   |  O ')
        print('   |  | ')
        print("___|     ")
    elif count == 3:
        print('    ___ ')    
        print('   |  O ')
        print('   |  | ')
        print("___| /   ")
    elif count == 4:
        print('    ___ ')    
        print('   |  O ')
        print('   |  | ')
        print("___| / \ ")
    elif count == 5:
        print('    ___ ')    
        print('   | \O ')
        print('   |  | ')
        print("___| / \ ")
    elif count == 6:
        print('    ___ ')    
        print('   | \O/')
        print('   |  | ')
        print("___| / \ ")
        
# Generate words
dictionary = []
filename = "SOWPODS.txt"
with open(filename, 'r') as open_file:
    for line in open_file:
        line = line.strip()
        dictionary.append(line)       
import random

# Play game
def playgame():        
    index = random.randint(1,len(dictionary))
    word = str(dictionary[index])
    count = 0
    guesses = set()
    print("Welcome to Hangman!")
    while count < 6:
        man(count)
        display(board(word,guesses))
        guess = str(input("Guess a letter:"))
        guess = guess.upper()
        if guess in guesses:
            print("You already guessed that!")
        elif guess not in word:
            print("Incorrect!")
            count += 1
        elif guess in word:
            print("Correct!")
        guesses.add(guess)
        if check(board(word,guesses)) == word:
            print(word)
            print("You win!")
            win()
            break
    if check(board(word,guesses)) != word:
        man(count)
        print("You lose!")
        print("The word was: ", word)

# Track wins
wins = 0
def win():
    global wins
    wins += 1

play = 1
while play == 1:
    playgame()
    play = int(input("Press 1 to play again: "))
if wins == 1:
    print("You won", wins, "time!")
else:
    print("You won", wins, "times!")
    