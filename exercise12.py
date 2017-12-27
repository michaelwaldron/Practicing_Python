# -*- coding: utf-8 -*-
"""
Practice Python Exercise 12

Get a list and return a list of only the first and last numbers.
Write it inside a function

"""

def first_last(list_in):
    list_out = []
    list_out.append(list_in[0])
    list_out.append(list_in[len(list_in)-1])
    print("First and last elements are:", list_out)

a = [1,2,3,4,5]
print("The original set is:", a)
b = first_last(a)