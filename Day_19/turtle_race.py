import random
from turtle import Turtle as t, Screen

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_X = -300
STARTING_Y = -130
FINISH_LINE_X = 350
TURTLE_SPACING = 50
RACE_DISTANCE = 300

def create_turtle(color):
    """Create and return a turtle with specified color"""
    turtle = t(shape="turtle")
    turtle.color(color)
    turtle.penup()
    return turtle

def draw_finish_line():
    """Draw the finish line aligned with the turtles"""
    finish_line = t()
    finish_line.penup()
    # Start at the topmost turtle's y position
    top_y = STARTING_Y + (len(COLORS) - 1) * TURTLE_SPACING
    finish_line.setposition(FINISH_LINE_X, top_y + 20)  # a little above the top turtle
    finish_line.pendown()
    finish_line.setheading(270)  # Point downwards
    # Draw down past the bottommost turtle
    finish_line.forward((len(COLORS) - 1) * TURTLE_SPACING + 40)
    finish_line.hideturtle()

def setup_race():
    """Initialize the race setup"""
    screen = Screen()
    screen.title("Turtle Race")

    # Set a fixed window size
    screen.setup(width=800, height=600)  
    
    # Get user's bet with validation
    while True:
        user_bet = screen.textinput(
            title="Make your bet",
            prompt=f"Which turtle will win the race? Enter a color: {', '.join(COLORS)}"
        ).lower()
        if user_bet in COLORS:
            break
        print("Invalid color! Please choose from the available colors.")
    
    return screen, user_bet

def main():
    # Create turtles
    turtles = [create_turtle(color) for color in COLORS]
    
    # Position turtles
    for i, turtle in enumerate(turtles):
        turtle.setposition(STARTING_X, STARTING_Y + (i * TURTLE_SPACING))
    
    # Setup screen and get bet
    screen, user_bet = setup_race()
    
    # Draw finish line
    draw_finish_line()
    
    # Race Loop
    race_is_on = True
    while race_is_on:
        for turtle in turtles:
            # Move the turtle forward by a random amount
            turtle.forward(random.randint(1, 10))  # Minimum of 1 to ensure movement
            
            # Check if the turtle has reached the finish line
            if turtle.xcor() > FINISH_LINE_X:
                race_is_on = False
                winner = turtle.pencolor()
                
                # Announce results
                if user_bet == winner:
                    print(f"🎉  You've won! The {winner} turtle is the winner!")
                else:
                    print(f"🥲  You've lost! The {winner} turtle is the winner!")
                break
    
    # Close the screen after a short delay
    screen.ontimer(screen.bye, 3000)  # Close after 3 seconds

if __name__ == "__main__":
    main()