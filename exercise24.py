# -*- coding: utf-8 -*-
"""
Practice Python Exercise 24

Create a 3 x 3 tic-tac-toe board in Python

"""

def board(dimensions):
    i = 0
    while i < dimensions:
        print(" ---"*int(dimensions))
        print("|   "*int(dimensions + 1))
        i += 1
    print(" ---"*int(dimensions))
        
# Tic-tac-toe size board
board(3)