# -*- coding: utf-8 -*-
"""
Practice Python Exercise 1

Ask users for name, age.
Print message telling them the year they'll turn 100.

"""

name = input("Please enter your name:")
age = input("Please enter your age:")
import datetime
now = datetime.datetime.now()
year = now.year
hundred = year + (100 - int(age))
print("Hi %s, you will turn 100 in the year %d" % (name, hundred))