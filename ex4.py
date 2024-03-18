# Purpose: 

def letter_places(str, letter):
    places = []
    start = 0
    while True:
        where = str.find(letter,start)
        if (where == -1):
            break
        places.append(where)
        start = where + 1
    return places

def nth(num):
    if num == 1:
        return str(num) + "st"
    if num == 2:
        return str(num) + "nd"
    if num == 3:
        return str(num) + "rd"
    return str(num) + "th"

user_input = input("Enter a message: ")
user_letter = input("What letter are you looking for? ")

places = letter_places(user_input, user_letter)

if len(places) == 0:
    print("That letter does not appear")
else:
    for place in places:
        print("That letter is the", nth(place+1), "letter")





