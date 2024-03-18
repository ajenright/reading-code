# Purpose: 

import random

def random_letter():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = letters + letters.upper()
    return random.choice(letters)

def random_number():
    numbers = '0123456789'
    return random.choice(numbers) 

howlong = input("How long do you want it to be? ")
out = ""

for char in range(int(howlong)):
    which = random.choice(["letter", "number"])
    if which == "letter":
        out = out + random_letter()
    else:
        out = out + random_number()

print(out)
