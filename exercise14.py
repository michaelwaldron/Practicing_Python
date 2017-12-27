# -*- coding: utf-8 -*-
"""
Practice Python Exercise 14

Ask user for a list, return list with no duplicates

"""
# Function to remove duplicates
def remove_dupes_a(list_in):
    no_dupes = list(set(list_in))
    print("The unique elements in this set are:", no_dupes)
    
# Function to remove duplicates
def remove_dupes_b(list_in):
    no_dupes = []
    for i in list_in:
        if i not in no_dupes:
            no_dupes.append(i)
    print("The unique elements in this set are:", no_dupes)
    
# Get list
lenlist1 = int(input("Please enter the size of your list:"))
list1 = []
while len(list1) < lenlist1:
    number = int(input("Please enter an element:"))
    list1.append(number)

# Use functions to remove duplicates    
remove_dupes_a(list1)
remove_dupes_b(list1)