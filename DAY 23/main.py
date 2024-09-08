import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car_list = []
STARTING_CAR_COUNT = 10

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.title("Turtle Crossing")

my_turtle = Player()
my_score = Scoreboard(level = 1, car_count = STARTING_CAR_COUNT)

screen.listen()
screen.onkeypress(lambda: my_turtle.move_forward(), "Up")

for _ in range(STARTING_CAR_COUNT):
    car_list.append(CarManager())

game_is_on = True
while game_is_on:
    
    time.sleep(0.1)

    for i in range(len(car_list)):
        car_list[i].move_left(my_score.level)
        if car_list[i].distance(my_turtle) <= 31:
            my_score.game_over()
            game_is_on = False
        
    if my_turtle.reached_finished_line():
        my_score.level += 1
        my_score.car_count +=1
        my_score.update_level()
        my_turtle.starting_position()
        car_list.append(CarManager())
        
    screen.update()
    
screen.exitonclick()
