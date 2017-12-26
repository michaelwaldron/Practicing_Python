# -*- coding: utf-8 -*-
"""
Practice Python Exercise 7

Ask for a list of numbers and return a list of those which are even

"""

# Get list, adapted from Exercise 5
lenlist = int(input("Please enter the length of your list of numbers:"))
list_in = []
for x in range(0, lenlist):
    if x < 1:
        get_num = int(input("Please enter the first item:"))
        list_in.append(get_num)
    else:
        get_num = int(input("Please enter another item:"))
        list_in.append(get_num)
        
# Return list of even numbers
evens = [number for number in list_in if number % 2 == 0]
print("The even numbers in your list are:", evens)