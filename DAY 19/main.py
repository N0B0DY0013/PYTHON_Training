from turtle import Turtle, Screen
import random

my_screen = Screen()
# my_turtle = Turtle()

# PHASE = 10
# my_turtle.shape("turtle")

# def forward():
#     my_turtle.forward(PHASE)

# def backward():
#     my_turtle.back(PHASE)
    
# def clockwise():
#     my_turtle.seth(my_turtle.heading() + (PHASE/2))
    
# def counter_clockwise():
#     my_turtle.seth(my_turtle.heading() - (PHASE/2))

# def clear():
#     # my_turtle.penup()
#     my_turtle.home()
#     my_turtle.clear()
    
#     # my_turtle.pendown()

# my_screen.listen()

# my_screen.onkeypress(forward,"w")
# my_screen.onkeypress(backward,"s")
# my_screen.onkeypress(counter_clockwise,"d")
# my_screen.onkeypress(clockwise,"a")
# my_screen.onkeypress(clear,"c")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

my_screen.setup(width=700, height=500)
user_bet = my_screen.textinput(title="Bet", prompt="Input which color: (Red, Orange, Yellow, Green, Blue, Violet)").lower()

colors = ["red", "orange", "yellow", "green", "blue", "violet"]
turtles = []

gap = 80
i = 0

for color in colors:
    cur_turtle = Turtle(shape="turtle")
    cur_turtle.color(color)
    cur_turtle.penup()
    cur_turtle.setpos(x=-320, y=(-200 + (i * gap)))
    
    turtles.append(cur_turtle)

    i += 1

no_one_reached_the_finish_line = True
bet_result = ""
winning_color = ""

while no_one_reached_the_finish_line:
    
    for ninja in turtles:
        
        ninja.forward(random.randint(1,10))
        
        if (ninja.xcor() + ninja.width()) >= ((my_screen.window_width() / 2) - 30):
            
            no_one_reached_the_finish_line = False
            winning_color = ninja.pencolor()
            if user_bet == ninja.pencolor().lower():
                bet_result = "win"
            else:
                bet_result = "lose"


print(f"Turtle race is finished! {winning_color.capitalize()} Turtle has won the race.\nYou {bet_result}.")
    
my_screen.exitonclick()