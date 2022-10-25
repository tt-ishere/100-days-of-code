import turtle as t
from turtle import Screen
import random

tt = t.Turtle()

t.colormode(255)
direction = [0,90, 180, 270]

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b
    

def move(distance):
    start = 0
    fin = 200
    while start != fin:
        tt.speed("fastest")
        tt.color(rand_color())
        tt.width(10)
        tt.forward(distance)
        tt.setheading(random.choice(direction))
        start += 1
        
move(15)

s = Screen()
s.exitonclick()
