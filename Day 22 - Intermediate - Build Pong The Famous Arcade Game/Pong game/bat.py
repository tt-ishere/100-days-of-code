from turtle import Turtle


class Bat(Turtle):
    def __init__(self, bat_position):
        super().__init__()
        self.create_bat(bat_position)
 
        
    def create_bat(self, bat_position):
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(bat_position)
        
    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

        
    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
