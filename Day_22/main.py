from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  


left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()
scoreboard = Scoreboard()


# Keyboard bindings
screen.listen()
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0:
        ball.bounce_x()

    # Detect collision with left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 and ball.x_move < 0:
        ball.bounce_x()

    # Detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

    # Game over condition
    if scoreboard.left_score == 5 or scoreboard.right_score == 5:
        game_is_on = False
        scoreboard.game_over()
    

screen.exitonclick()

