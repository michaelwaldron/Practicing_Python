# -*- coding: utf-8 -*-
"""
Practice Python Exercise 10

Revisit Exercise 5 and use list comprehensions to make the code shorter.
(Get two random lists and return a list of common elements)
I left 'get lists' longer so it can be dynamic.

"""

# Get lists
lenlist1 = int(input("Please enter the size of your first list:"))
list1 = []
while len(list1) < lenlist1:
    number = int(input("Please enter an element:"))
    list1.append(number)

lenlist2 = int(input("Please enter the size of your second list:"))
list2 = []
while len(list2) < lenlist2:
    number = int(input("Please enter an element:"))
    list2.append(number)
    
# Create common lists
commmonlist = [a for a in list1 for b in list2 if a==b]
print("The common elements are:", commmonlist)