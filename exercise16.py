# -*- coding: utf-8 -*-
"""
Practice Python Exercise 16

Generate a password for the user. Ask them how strong they want it to be.

"""

# ASCII ranges
symbols = [33,35,36,37,38,63,64]
uppers = list(range(65,90))
lowers = list(range(97,122))
numbers = list(range(48,57))

# Password generator
def gen_pw(strength):
    import random
    track = 0
    password = ""
    while track < strength:
        choose = random.randint(1,10)
        if choose in range(1,2):
            password += chr(random.choice(uppers))
        elif choose in range(3,9):
            password += chr(random.choice(lowers))
        else:
            password += chr(random.choice(symbols))
        track += 1
    return password

# User interface
strength = int(input("How many characters would you like in your password? "))  
password = gen_pw(strength)
print("Your password is:", password)