# -*- coding: utf-8 -*-
"""
Practice Python Exercise 30

Write a function to grab a random word from the Scrabble dictionary.
File: SOWPODS.txt

"""

# Dictionary of Scrabble words
dictionary = []
filename = "SOWPODS.txt"
with open(filename, 'r') as open_file:
    for line in open_file:
        line = line.strip()
        dictionary.append(line)

# Print random word        
import random
index = random.randint(1,len(dictionary))
print(dictionary[index])