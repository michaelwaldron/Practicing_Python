# -*- coding: utf-8 -*-
"""
Practice Python Exercise 34

Load birthdays from JSON file, allow user to add new JSON entries

"""

import json

birthday = {}
with open('birthdays.json', 'r') as f:
          birthday = json.load(f)

# Add entry
def add():
    name = input('Who would you like to add? ')
    date = input('When was {} born? '.format(name))
    birthday[name] = date
    with open('birthdays.json', 'w') as f:
        json.dump(birthday, f)
    print('{} was added to the dictionary.'.format(name))
          
# Find entry
def find():
    name = input('Whose birthday should we find? ')
    try:
        if birthday[name]:
            print('{} was born on {}'.format(name, birthday[name]))
    except KeyError:
        print('{} is not in the list\n'.format(name))
          
# List entries
def allent():
    print('Current birthdays in the list are:\n_______________________________')
    for key in birthday:
        print(key,':', birthday[key])

# Control
while True:
    what_next = input('What do you want to do next? you can: Add, Find, List, Quit\n').capitalize()
    if what_next == 'Quit':
        print('Good Bye')
        break
    elif what_next == 'Add':
        add()
    elif what_next == 'Find':
        find()
    elif what_next == 'List':
        allent()