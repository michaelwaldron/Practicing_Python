# -*- coding: utf-8 -*-
"""
Practice Python Exercise 11

Get a number from the user and determine whether it is prime or not.
(Build off exercise 4)

"""

number = int(input("Please enter an integer:"))
divisors = 0
check = 1

while check <= number:
    if number % check == 0:
        divisors += 1
        check += 1
    else:
        check += 1

if divisors == 2:
    print("Congrats!", number, "is a prime number.")
else:
    print(number, "is not a prime number.")