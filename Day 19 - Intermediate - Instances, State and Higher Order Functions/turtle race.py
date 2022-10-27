from random import randint, random
from turtle import Turtle, Screen
import turtle

is_race_on = False
sc = Screen()
sc.setup(width=500, height=400)
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
user_chioce = sc.textinput(title="Chose the winner", prompt="Which turtle will win the race? Enter it's color.")
y  = 100

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(-230, y )
    all_turtles.append(new_turtle)
    y -= 40

if user_chioce:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_chioce:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        
sc.exitonclick()
