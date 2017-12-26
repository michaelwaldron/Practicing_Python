# -*- coding: utf-8 -*-
"""
Practice Python Exercise 8

Rock-Paper-Scissors

"""
import time
def wait(x):
    time.sleep(x)
    return

# Converse
print("Welcome to Rock-Paper-Scissors!\n")
wait(1)
player1 = str(input("Player 1, enter your name:\n"))
wait(.5)
print("Welcome, %s." % player1)
wait(1)
player2 = str(input("Player 2, enter your name:\n"))
wait(.5)
print("Welcome, %s." % player2)
wait(1)
rounds = int(input("How many rounds should we play?"))
wait(1)
print("Great, remember:")
wait(0.75)
print("'R' is for rock, 'P' is for paper, and 'S' is for scissors.")
wait(3)
print("Let's get started!")

# Play
round = 0
p1 = 0
p2 = 0
draw = 0
while round < rounds:
    p1move = str(input("Player 1, enter 'R,' 'P,' or 'S':"))
    p2move = str(input("Player 2, enter 'R,' 'P,' or 'S':"))
    if p1move == p2move:
        draw += 1
        print("Round %s is a draw!" % str(round+1))
        round += 1
    elif (p1move == 'R' and p2move == 'S') or (p1move == 'S' and p2move == 'P') or (p1move == 'P' and p2move == 'R'):
        p1 += 1
        print("Player 1 wins round %s!" % str(round+1))
        round += 1
    elif (p2move == 'R' and p1move == 'S') or (p2move == 'S' and p1move == 'P') or (p2move == 'P' and p1move == 'R'):
        p2 += 1
        print("Player 2 wins round %s!" % str(round+1))
        round +=1
    else:
        print("Please enter a valid letter!")

# Score
wait(1)
if p1 > p2:
    print("Game over. Player 1 wins, going %d-%d-%d." % (p1, p2, draw))
elif p2 > p1:
    print("Game over. Player 2 wins, going %d-%d-%d." % (p2, p1, draw))
else:
    print("Tie game! Player 1 won %d, Player 2 won %d, and there were %d ties." % (p1, p2, draw))