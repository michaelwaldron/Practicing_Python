# -*- coding: utf-8 -*-
"""
Practice Python Exercise 35

Print number of birthdays in each month

"""

num_to_string = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}

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
    print(months[month], 'birthday(s) in', num_to_string[month])