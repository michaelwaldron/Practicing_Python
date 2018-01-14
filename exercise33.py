# -*- coding: utf-8 -*-
"""
Practice Python Exercise 33

Birthday Dictionary

"""

# Set up dictionary
birthdays = {}

# Get birthdays
more = 1
while more == 1:
    person = str(input("Enter a person's name: "))
    birthday = str(input("Enter their birthday: "))
    birthdays[person] = birthday
    more = int(input("Enter 1 to add another birthday: "))

# Lookup birthdays
go = 1
while go == 1:
    lookup = str(input("Who's birthday should we look up? "))
    birthday = birthdays.get(lookup, "not in our dictionary.")
    print(lookup, "'s birthday is", birthday)
    go = int(input("Enter 1 to look up another birthday: "))