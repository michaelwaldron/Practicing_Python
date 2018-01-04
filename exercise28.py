# -*- coding: utf-8 -*-
"""
Practice Python Exercise 28

Max of three. Get three numbers, return the max without the max function.

"""
nums = []
while len(nums) < 3:
    nums.append(int(input("Please enter a number: ")))
largest = -(10**10)
for num in nums:
    if num > largest:
        largest = num
print("The largest number is", largest)

# Could have written this as a function with three inputs, as below
def max_of_three(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    print("The largest number is", largest)
    return largest

max_of_three(42,69,100)