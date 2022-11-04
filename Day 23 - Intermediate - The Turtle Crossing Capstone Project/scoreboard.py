from turtle import Turtle

FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.high_score = 0
        self.penup()
        self.update_score()
        
    def update_score(self):
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align='center', font=FONT)

def high_score(self):
    
    pass
