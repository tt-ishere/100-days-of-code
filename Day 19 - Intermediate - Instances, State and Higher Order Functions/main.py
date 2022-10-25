from turtle import Turtle, Screen

tt = Turtle()
sc = Screen()
sc.listen()

def forward():
    tt.forward(10)


def backward():
    tt.back(10)
    
def anticlockwise():
    tt.left(5)
    
def clockwise():
    tt.right(5)

def clear():
    tt.reset()
sc.onkey(key="f", fun=forward)
sc.onkey(key="s", fun=backward)
sc.onkey(key="a", fun=anticlockwise)
sc.onkey(key="d", fun=clockwise)
sc.onkey(key="c", fun=clear)


sc.exitonclick()