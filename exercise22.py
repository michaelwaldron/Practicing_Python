# -*- coding: utf-8 -*-
"""
Practice Python Exercise 22

Read names from file. Store each unique and count its occurrences.
(File: nameslist.txt, downloaded from website)

"""
# Dictionary for names
names = {}

# Count names from file
filename = "nameslist.txt"
with open(filename, 'r') as open_file:
    for line in open_file:
        line = line.strip()
        if line not in names:
            names[line] = 1
        else:
            names[line] +=1
    
# Print dictionary
for pair in names.items():
    print(pair)