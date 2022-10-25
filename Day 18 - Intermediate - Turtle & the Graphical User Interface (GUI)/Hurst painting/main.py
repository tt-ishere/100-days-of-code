# import colorgram
import random
from turtle import Turtle, Screen
import turtle

# # Extracting rgb colors
# extracted_colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in extracted_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)

rgb_colors = [(245, 241, 233), (227, 234, 242), (245, 234, 239), (233, 242, 236), (208, 158, 96), (234, 213, 101),
              (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55),
              (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36),
              (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167),
              (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]

tt = Turtle()
turtle.colormode(255)
tt.speed('fastest')
y = -250.00

for y_axis in range(10):
    tt.penup()
    tt.goto(-250.00, y)
    for x_axis in range(10):
        tt.dot(20, random.choice(rgb_colors))
        tt.penup()
        tt.forward(50)
    y += 50.00


tt.hideturtle()
screen = Screen()
screen.exitonclick()
