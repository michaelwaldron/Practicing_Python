# -*- coding: utf-8 -*-
"""
Practice Python Exercise 13

Ask user how many Fibonacci numbers he wants, then generate them.

"""
def gen_fib(size):
    if size == 0:
        fib = []
        return fib
    elif size == 1:
        fib = [0]
        return fib
    elif size == 2:
        fib = [0,1]
        return fib
    else:
        i = 0
        fib = [0,1]
        while i + 2 < size:
            fib_next = fib[i+1] + fib[i]
            fib.append(fib_next)
            i+=1
        return fib

user_in = int(input("How many Fibonacci numbers would you like?"))
fib = gen_fib(user_in)
print("The first", user_in, "Fibonacci numbers are:", fib)