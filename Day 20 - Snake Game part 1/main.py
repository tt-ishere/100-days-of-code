from turtle import Screen, Turtle

new_turtle = Turtle()
sc = Screen()
sc.setup(width=600, height=600)
sc.title('Snake Game')
sc.bgcolor('black')
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segment = []


for position in starting_position:
    new_turtle = Turtle('square')
    new_turtle.color('white')
    new_turtle.goto(position)
    segment.append(new_turtle)
    
sc.exitonclick()