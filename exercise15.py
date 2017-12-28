# -*- coding: utf-8 -*-
"""
Practice Python Exercise 15

Get a string and return the words in reverse order.

"""
def reverse(string):
    return " ".join(string.split()[::-1])


phrase = str(input("Please enter a phrase:"))
print(reverse(phrase))