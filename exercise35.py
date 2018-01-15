# -*- coding: utf-8 -*-
"""
Practice Python Exercise 35

Print number of birthdays in each month

"""

import json

birthday = {}
with open('birthdays.json', 'r') as f:
          birthday = json.load(f)

months = {}
for month in range(1,13):
    months[month] = 0

for key in birthday:
    if birthday[key][1] == '/':
        index = int(birthday[key][0])
        months[index] += 1
    elif birthday[key][2] == '/':
        index = int(birthday[key][0])*10 + int(birthday[key][1])
        months[index] += 1

for month in months:
    print(months[month], 'birthday(s) in month', month)