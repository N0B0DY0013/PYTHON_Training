
from turtle import Turtle, Screen
import pandas

IMG_NAME = "blank_states_img.gif"
guessed_states = []

my_screen = Screen()
my_turtle = Turtle()

my_screen.title("U.S. States Game")
my_screen.addshape(IMG_NAME)

my_turtle.shape(IMG_NAME)

us_states_data = pandas.read_csv("50_states.csv")

while len(guessed_states) < 50:
    
    guessed_state = my_screen.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt = "Please enter a state name:").title()
    
    if guessed_state == "Exit":
        break
    
    try:
        index = us_states_data["state"].to_list().index(guessed_state)
    except:
        index = -1
    
    if index > -1:
        if guessed_state not in guessed_states:
            state_turtle = Turtle()
            state_turtle.penup()
            state_turtle.hideturtle()
            state_turtle.goto(x = int(us_states_data["x"].to_list()[index]), y = int(us_states_data["y"].to_list()[index]))
            state_turtle.write(guessed_state)
            
            guessed_states.append(guessed_state)


not_guessed_state = us_states_data["state"][~us_states_data["state"].isin(guessed_states)].to_list()

pandas.DataFrame.from_dict({"Unguessed States": not_guessed_state}).to_csv("unguessed_states.csv")


my_screen.exitonclick()