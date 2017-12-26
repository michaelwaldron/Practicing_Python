# -*- coding: utf-8 -*-
"""
Practice Python Exercise 5

Write a program that takes two lists and returns a list of common elements.

"""

# Get lists
lenlist1 = int(input("Please enter the length of List 1:"))
list1 = []
for x in range(0, lenlist1):
    get_num = int(input("Please enter an item:"))
    list1.append(get_num)
lenlist2 = int(input("Please enter the length of List 2:"))
list2 = []
for x in range(0, lenlist2):
    get_num = int(input("Please enter an item:"))
    list2.append(get_num)

# Create common list
commonlist = []
for num_1 in list1:
    for num_2 in list2:
        if num_1 == num_2:
            commonlist.append(num_2)
print("The common elements are:")
print(commonlist)