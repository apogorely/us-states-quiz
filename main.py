from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("US Game")
screen.tracer(0)
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)

states = pd.read_csv("50_states.csv")
state_names = states.state.to_list()

score = 0

# State Name Turtle
def create_name(state_name, x_position, y_position):
    staat = Turtle()
    staat.hideturtle()
    staat.penup()
    staat.setposition(int(x_position), int(y_position))
    staat.write(state_name, align="center", font=("Arial", 12, "normal"))

screen.update()
while score < len(state_names):
    user_input = screen.textinput(title=f"Name a State {score}/{len(state_names)}", prompt="Guess a state in the US: ").title()
    for state in state_names:
        if user_input == state:
            entry = states[states.state == state]
            create_name(state, entry.x, entry.y)
            score += 1

screen.exitonclick()
