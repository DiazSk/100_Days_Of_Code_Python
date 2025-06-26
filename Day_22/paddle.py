from turtle import Turtle

# Constants
PADDLE_WIDTH = 20
PADDLE_LENGTH = 100
X_POSITION_LEFT = -350
X_POSITION_RIGHT = 350
Y_POSITION = 0


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        """Create the paddle at specified position"""
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if position == "left":
            self.goto(X_POSITION_LEFT, Y_POSITION)
        elif position == "right":
            self.goto(X_POSITION_RIGHT, Y_POSITION)

    def go_up(self):
        """Move the paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Move the paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


