from turtle import Screen, Turtle
import random

tt = Turtle()
tt.shape("arrow")
colours =["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen", "Violet", "Red", "Green", "Yellow"]
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

# # TODO 3 Draw multiple shapes

# def angle(sides):
#     return 360.0 / sides

# sides = 3.0
# while sides != 10.0: 
#     for _ in range(int(sides)):
#         tt.color(random.choice(colours))
#         tt.forward(100)
#         tt.right(angle(sides))
#     sides += 1.0

# TODO 4 Random walk

direction = [0,90, 180, 270]

def move(distance):
    start = 0
    fin = 200
    while start != fin:
        tt.speed("fast")
        tt.color(random.choice(colours))
        tt.width(1)
        tt.forward(distance)
        tt.setheading(random.choice(direction))
        start += 1
    
        

move(30)
screen = Screen()
screen.exitonclick()
