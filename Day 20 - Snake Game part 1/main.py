from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

sc = Screen()
sc.setup(width=600, height=600)
sc.title('Snake Game')
sc.bgcolor('black')
sc.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

sc.listen()
# listens to the direction keys 
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    sc.update() 
    time.sleep(0.10) 
    snake.move() 
   
#    Detect colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # Detect colision with wall
    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        game_is_on = False
        scoreboard.game_over()
    
    # Detect colision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
           
sc.exitonclick()
