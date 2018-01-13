# -*- coding: utf-8 -*-
"""
Practice Python Exercise 29

Full Tic-Tac-Toe game. Optional: keep track of overall wins.

"""

# Implement using exercises 24 (board), 26 (check), 27 (move)

# Print Board Function
def display(dimensions, game):
    i = 0
    while i < dimensions:
        print(" -----"*int(dimensions))
        print("| ",game[i][0]," | ",game[i][1]," | ",game[i][2]," |")
        i += 1
    print(" -----"*int(dimensions))

# Checks status of a Tic-Tac-Toe board
def player(spot):
    if spot == 'X':
        print("Player 1 wins!")
        return(1)
    elif spot == 'O':
        print("Player 2 wins!")
        return(2)
def catgame(board):
    cat = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == ' ':
                cat += 1
    if cat == 0:
        return 1
    else:
        return 0
def check(board):
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        player(board[0][0])
        if player(board[0][0]) == 1:
            return 1
        elif player(board[0][0]) == 1:
            return 2
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        player(board[0][0])
        if player(board[0][0]) == 1:
            return 1
        elif player(board[0][0]) == 1:
            return 2
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        player(board[0][0])
        if player(board[0][0]) == 1:
            return 1
        elif player(board[0][0]) == 1:
            return 2
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        player(board[2][0])
        if player(board[2][0]) == 1:
            return 1
        elif player(board[2][0]) == 1:
            return 2
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        player(board[2][0])
        if player(board[2][0]) == 1:
            return 1
        elif player(board[2][0]) == 1:
            return 2
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        player(board[1][0])
        if player(board[1][0]) == 1:
            return 1
        elif player(board[1][0]) == 1:
            return 2
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        player(board[0][1])
        if player(board[0][1]) == 1:
            return 1
        elif player(board[0][1]) == 1:
            return 2
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        player(board[0][2])
        if player(board[0][2]) == 1:
            return 1
        elif player(board[0][2]) == 1:
            return 2
    elif catgame(board) == 1:
        print("Cat game, nobody wins!")
        return 3
   
# Wait function
import time
def wait(x):
    time.sleep(x)
    return

# Get next move
def get_move(moves):
    player = (moves % 2) + 1
    if player == 1:
        move = str(input("Player 1, please enter your move in 'row, column' format:"))
    elif player == 2:
        move = str(input("Player 2, please enter your move in 'row, column' format:"))
    move = move.split(",")
    return move

# Game script
playgame = int(input("Press 1 to play: "))
p1wins = 0
p2wins = 0
while playgame == 1:
    game = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    moves = 0
    over = 0
    while moves < 9 and over != 1:
        move = get_move(moves)
        row = int(move[0]) - 1
        col = int(move[1]) - 1
        if game[row][col] != ' ':
            print("That space is already taken. Choose a different one.")
            moves -= 1
            wait(1)
        elif moves == 0 or moves % 2 == 0:
            game[row][col] = 'X'
        elif moves % 2 != 0:
            game[row][col] = 'O'
        display(3, game)
        check(game)
        if check(game) == 1 or check(game) == 2 or check(game) == 3:
            over = 1
            if check(game) == 1:
                p1wins += 1
            if check(game) == 2:
                p2wins += 1
        moves += 1
    print("Player 1 has", p1wins,"wins, Player 2 has", p2wins,"wins.")
    playgame = int(input("Enter 1 to keep playing: "))