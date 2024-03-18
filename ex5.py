# Purpose: 

import random
from turtle import *

def star(size, star_color):
    old_color = fillcolor()
    fillcolor(star_color)
    begin_fill()
    for i in range(5):
        forward(size)
        left(72)
        forward(size)
        right(144)
    end_fill()
    fillcolor(old_color)

def get_restaurants():
    restaurant_list = []
    while True:
        rest = input("What is a restaurant you like? ")
        if rest == "":
            return restaurant_list
        restaurant_list.append(rest)

def draw_list(restaurants, choice):
    for rest in restaurants:
        write(rest, font=("Arial", 20, "normal"))
        if rest == choice:
            penup(); back(50); left(90); forward(25); right(90); pendown()
            star(20, "red")
            penup(); right(90); forward(25); left(90); forward(50); pendown()
        penup(); right(90); forward(50); left(90); pendown()



rest_list = get_restaurants()
rest_list.sort()
to_go_to = random.choice(rest_list)
draw_list(rest_list, to_go_to)

done()

        
