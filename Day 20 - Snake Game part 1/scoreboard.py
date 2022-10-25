from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0.0, 270.0)
        self.score = 0
        self.update_score()
        
        
    def update_score(self):
        self.write(arg= f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # increases the score
        self.clear()
        self.score += 5
        self.update_score()
        
    def game_over(self):
        # ends game
        self.goto(0.0, 0.0)
        self.write(arg= "GAME OVER", align=ALIGNMENT, font=FONT)
        
    