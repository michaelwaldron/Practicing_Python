# -*- coding: utf-8 -*-
"""
Practice Python Exercise 13

Ask user how many Fibonacci numbers he wants, then generate them.

"""

def next_num(current_num, previous_num):
    holder = previous_num + current_num
    return holder

amount = int(input("Enter the amount of Fibonacci numbers you want:"))
fib_series = [0,1]
tracker = 2
while tracker < amount:
    current_num = fib_series[tracker-1]
    previous_num = fib_series[tracker-2]
    fib_series.append(next_num(current_num, previous_num))
    tracker += 1
print("Fibonacci series up to", amount, "elements:", fib_series)