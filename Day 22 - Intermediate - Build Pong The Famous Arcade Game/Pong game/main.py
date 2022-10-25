from turtle import Screen, Turtle
from bat import Bat
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

scoreboard = Scoreboard()
l_bat = Bat((-350, 0))
r_bat = Bat((350, 0))
ball = Ball()

    
screen.listen()
# left bat
screen.onkey(l_bat.go_up, "w")
screen.onkey(l_bat.go_down, "s")

# right bat
screen.onkey(r_bat.go_up, "Up")
screen.onkey(r_bat.go_down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
     
    # detect colission with bats 
    if ball.distance(r_bat) < 50 and ball.xcor() > 320 or ball.distance(l_bat) < 50 and ball.xcor() < -320:
        ball.bounce_x()
     
    # detect if left bat misses the ball 
    if ball.xcor() < -395:
        ball.refresh()
        scoreboard.r_point()
           
    # detect if right bat misses the ball 
    if ball.xcor() > 395:
        ball.refresh()
        scoreboard.l_point()
        
screen.exitonclick() 
