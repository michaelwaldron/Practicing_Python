# -*- coding: utf-8 -*-
"""
Practice Python Exercise 27

Store the active Tic-Tac-Toe board.
Allow 2 players to fill in X's and O's, respectively

"""
# Wait function
import time
def wait(x):
    time.sleep(x)
    return

# Get next move
def get_move():
    move = str(input("Please enter your move in 'row, column' format:"))
    move = move.split(",")
    return move

# Initiate game
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
moves = 0

# Play game
while moves < 9:
    move = get_move()
    row = int(move[0]) - 1
    col = int(move[1]) - 1
    if game[row][col] != 0:
        print("That space is already taken. Choose a different one.")
        moves -= 1
        wait(1)
    elif moves == 0 or moves % 2 == 0:
        game[row][col] = 'X'
    elif moves % 2 != 0:
        game[row][col] = 'O'
    print(game)
    moves += 1
    wait(1)