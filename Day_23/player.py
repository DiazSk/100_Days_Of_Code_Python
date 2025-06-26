from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")
ALIGN = "center"

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.create_player()

    
    def create_player(self):
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)


    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def move(self):
        self.forward(MOVE_DISTANCE)


    def game_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.write("Game Over", align=ALIGN, font=FONT)
    

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False    