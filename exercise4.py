# -*- coding: utf-8 -*-
"""
Practice Python Exercise 4*
*3 skipped because of low difficulty

Ask for a number and print all divisors of that number.

"""

num_in = int(input("Please enter an integer:"))
numbers = range(1, num_in + 1)
num = str(num_in)
divisors = []
for number in numbers:
    if num_in % number == 0:
        divisors.append(number)
print("The divisors of %s are:" % num)
print(divisors)