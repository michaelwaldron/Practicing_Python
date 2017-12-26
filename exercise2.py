# -*- coding: utf-8 -*-
"""
Practice Python Exercise 2

Even or Odd

"""

number = int(input("Please enter an integer:"))
if number % 2 == 0:
    numstr = str(number)
    print("%s is an even number" % numstr)
else:
    numstr = str(number)
    print("%s is an odd number" % numstr)