from turtle import Screen, Turtle
import random
import turtle


tt = Turtle()
s = Screen()
tt.speed("fastest")
turtle.colormode(255)


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b

def spirograph(gap):
    for i in range(int(360 / gap)):
        tt.color(rand_color())
        tt.circle(100)
        tt.right(gap)
    tt.hideturtle()


spirograph(5)
s.exitonclick()
