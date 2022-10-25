from turtle import Screen, Turtle
import random

tt = Turtle()
tt.shape("arrow")
tt.color("violet")

# # TODO 1 Draw a square 
# for i in range(0,4):
#     tt.forward(100)
#     tt.right(90)

# # TODO 2 Draw dashed line
# for i in range(0,50):
#     tt.penup()
#     tt.forward(10)
#     tt.pendown()
#     tt.forward(10)

# TODO 3 Draw multiple shapes

# def angle(sides):
#     return 360.0 / sides

# sides = 3.0
# while sides != 10.0: 
#     for _ in range(int(sides)):
#         tt.forward(100)
#         tt.right(angle(sides))
#     sides += 1.0

# TODO 4 Random walk

direction = [tt.backward,tt.forward, tt.left, tt.right]
# path = random.choice(direction)
# print(path)

def move(distance):
    start = 0
    fin = 500
    while start != fin:
        path = random.choice(direction)
        path(distance)
        tt.width(1)
        tt.resizemode('auto')
        start += 1
    
        

move(90)
screen = Screen()
screen.exitonclick()
