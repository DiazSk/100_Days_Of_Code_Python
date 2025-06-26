import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("US States Game")
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

# Read the CSV file
data = pd.read_csv("50_states.csv")

# Get all the states from the CSV file
all_states = data.state.to_list()

# Create a list to store the guessed states
guessed_states = []

# Loop through the states and check if the user has guessed them all
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                  prompt="What's another state's name?")
    
    # Handle cancel button (None returned)
    if answer_state is None:
        break
    
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

# End game message
if len(guessed_states) == 50:
    final_turtle = turtle.Turtle()
    final_turtle.hideturtle()
    final_turtle.penup()
    final_turtle.goto(0, 0)
    final_turtle.write("Congratulations! You got all 50 states!", align="center", 
                      font=("Arial", 24, "bold"))

screen.exitonclick()