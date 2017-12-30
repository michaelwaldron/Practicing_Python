# -*- coding: utf-8 -*-
"""
Practice Python Exercise 20

Get an ordered list of numbers. Get an element. Determine if element in list.
(Optional: use binary search)

"""
# Compare
def compare(user_in, list_in):
    for element in list_in:
        if element == user_in:
            return True
    return False

# Get list
lenlist = int(input("Please enter the length of your list of numbers:"))
list_in = []
print("Please enter your numbers smallest to largest.\n")
for x in range(0, lenlist):
    get_num = int(input("Please enter an item:"))
    list_in.append(get_num)

# Make comparison
user_in = int(input("Please enter the number to check:"))
result = compare(user_in, list_in)
if result == True:
    print("Congrats! %d is on the list." % user_in)
else:
    print("Sorry, %d is not on the list." % user_in)