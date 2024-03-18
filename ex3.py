# Purpose: 


from turtle import *

def bar(bar_color):
    old_fill = fillcolor()
    old_pen = pencolor()
    color(bar_color)
    begin_fill()
    forward(300)
    left(90)
    forward(10)
    left(90)
    forward(300)
    left(90)
    forward(10)
    left(90)
    end_fill()
    color(old_pen, old_fill)

def box(box_color):
    color(box_color)
    begin_fill()
    for i in range(4):
        forward(70)
        right(90)
    end_fill()


def next():
    penup()
    right(90)
    forward(10)
    left(90)
    pendown()

speed(9)

for i in range(6):
    bar("red")
    next()
    bar("white")
    next()
bar("red")
next()

penup(); goto(0,11); pendown()
box("blue")

done()
