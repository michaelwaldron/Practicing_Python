# -*- coding: utf-8 -*-
"""
Practice Python Exercise 23

Take two .txt files of numbers and return the common elements.
(happynumbers.txt and primenumbers.txt)

"""

# Function to return list of integers
def txt_to_int_list(filename):
    list_to_return = []
    with open(filename, 'r') as open_file:
        for line in open_file:
            line = line.strip()
            list_to_return.append(int(line))
    return list_to_return

# Get lists
primes = txt_to_int_list('primenumbers.txt')
happy = txt_to_int_list('happynumbers.txt')

# List comprehension
common = [a for a in primes if a in happy]
print('The common elements are:', common)