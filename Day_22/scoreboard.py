from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.create_scoreboard()
        self.update_scoreboard()

    def create_scoreboard(self):
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.left_score}", align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.right_score}", align="center", font=("Courier", 80, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.penup()
        self.hideturtle()
        self.write("GAME OVER!", align="center", font=("Courier", 60, "bold"))
        self.goto(0, -60)
        self.write(f"Final Score: {self.left_score} - {self.right_score}", align="center", font=("Courier", 40, "normal"))
