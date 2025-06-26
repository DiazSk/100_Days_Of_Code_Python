from turtle import Turtle, Screen

tim = Turtle()
tom = Turtle()
tom.color("red")
tom.penup()
tom.setposition(0, 100)

screen = Screen()

def move_forward():
    tim.forward(100)

def move_backward():
    tim.backward(100)

def turn_left():
    tim.left(20)

def turn_right():
    tim.right(20)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
