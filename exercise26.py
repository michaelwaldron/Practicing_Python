# -*- coding: utf-8 -*-
"""
Practice Python Exercise 26

Tic-Tac-Toe check.

"""
# Called by Check to determine who won
def player(spot):
    if spot == 1:
        print("Player 1 wins!")
    elif spot == 2:
        print("Player 2 wins!")

# Called by Check to determine if cat game
def catgame(board):
    cat = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == 0:
                cat += 1
    if cat == 0:
        return 1
    else:
        return 0
            
# Checks the status of a Tic-Tac-Toe board
def check(board):
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        player(board[0][0])
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        player(board[0][0])
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        player(board[0][0])
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        player(board[2][0])
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        player(board[2][0])
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        player(board[1][0])
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        player(board[0][1])
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        player(board[0][2])
    elif catgame(board) == 1:
        print("Cat game, nobody wins!")
    else:
        print("No winners yet, keep playing!")
    

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
check(winner_is_2)

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
check(winner_is_1)

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]
check(no_winner)

cat_game = [[1, 2, 1],
	[2, 1, 2],
	[2, 1, 2]]
check(cat_game)