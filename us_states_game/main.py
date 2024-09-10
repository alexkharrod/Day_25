import turtle
from turtle import Turtle, Screen

import pandas as pd

def write_answer(state, x, y):
    draw_turtle.goto(x,y)
    draw_turtle.write(state, move=False, align="center")

def state_info(state_to_draw):
    state_stats = df[df['state'] == state_to_draw]
    xcor = state_stats['x'].values[0]
    ycor = state_stats['y'].values[0]
    write_answer(state_to_draw, xcor, ycor)


draw_turtle = Turtle()
draw_turtle.hideturtle()
draw_turtle.penup()


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


df = pd.read_csv("50_states.csv")
all_states = df.state.values
guessed_correct = []

while len(guessed_correct) < 50:

    # get user to make a guess
    answer_state = screen.textinput(title=f"Guess the state.  {len(guessed_correct)} / 50 correct", prompt="What's another states name?").title()
    if answer_state == "Exit":
        break
    # check to see if answer stats is in df 'states'. if it is draw and continue, if not continue
    if answer_state in df['state'].values:
        state_info(answer_state)
        guessed_correct.append(answer_state)
did_not_guess =[]
for state in all_states:
    if state not in guessed_correct:
        did_not_guess.append(state)

state_dict = {"state": did_not_guess}
states_to_learn = pd.DataFrame(state_dict)
print(state_dict)

states_to_learn.to_csv('states_to_learn.csv')



