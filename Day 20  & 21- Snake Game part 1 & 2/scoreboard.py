from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0.0, 270.0)
        self.write(arg=f"SCORE: {self.score}     HIGHSCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 5
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()
