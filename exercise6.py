# -*- coding: utf-8 -*-
"""
Practice Python Exercise 6

Get string from user and determine whether it is a palindrome.

"""

rawstr = input("Please enter a word or phrase without punctuation:")
clstr = rawstr.replace(" ","")
string = clstr.lower()
forstr = []
revstr = []
length = len(string)
for i in range(0,length):
    forstr.append(string[i])
    revstr.append(string[length-i-1])
for i in range(0,length):
    count = 0
    if not forstr[i] == revstr[i]:
        count += 1
if count == 0:
    print("'%s' is a palindrome!" % rawstr)
else:
    print("'%s' is not a palindrome..." % rawstr)
    
# Could have been done more simply with:
# string = str(rawstr)
# revstr = string[::-1]