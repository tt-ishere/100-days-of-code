from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()
        self.speed(10)
        

       
    def refresh(self):
        # put food at random locations  within screen boundary(600 x 600)
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)
        