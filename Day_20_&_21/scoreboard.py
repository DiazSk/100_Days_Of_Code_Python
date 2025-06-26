from turtle import Turtle

# Constants
SCOREBOARD_POSITION = (0, 270)
SCOREBOARD_FONT = ("Courier", 24, "normal")
SCOREBOARD_ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt", mode="r") as file:
                data = file.read()
                self.high_score = int(data) if data.strip() else 0
        except (FileNotFoundError, ValueError):
            self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard display with current score and high score."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=SCOREBOARD_ALIGN, font=SCOREBOARD_FONT)

    def update_score(self):
        """Increment the score and update the display."""
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        """Reset the score and update high score if needed."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
    
    def game_over(self):
        """Display game over message."""
        self.goto(0, 0)
        self.write("GAME OVER", align=SCOREBOARD_ALIGN, font=SCOREBOARD_FONT)

    def increase_score(self):
        """Increment the score."""
        self.score += 1
        self.update_scoreboard()
    


