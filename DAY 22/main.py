from turtle import Turtle, Screen
from paddle import Paddle
from pong_ball import PongBall
from score_board import ScoreBoard
import time

BASE_SPEED = 0.04
time_speed = BASE_SPEED

continue_playing = True

def end_game():
    global continue_playing
    continue_playing = False
    exit()

my_screen = Screen()

my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("PONG")
my_screen.tracer(0)
my_screen.listen()

paddle_one = Paddle(stretch_width = 5, stretch_length = 1, x_pos = 350, y_pos = 0, screen = my_screen, paddle_color = "red")

paddle_two = Paddle(stretch_width = 5, stretch_length = 1, x_pos = -350, y_pos = 0, screen = my_screen, paddle_color = "blue")

pong_ball = PongBall(x_pos = 0, y_pos = 0, screen = my_screen)

my_scoreboard = ScoreBoard()

my_screen.update()

my_screen.onkeypress(lambda: paddle_two.move_up(), "w")
my_screen.onkeypress(lambda: paddle_one.move_up(), "Up")

my_screen.onkeypress(lambda: paddle_two.move_down(), "s")
my_screen.onkeypress(lambda: paddle_one.move_down(), "Down")
    
my_screen.onkeypress(end_game, "Escape")

while continue_playing:
    
    if pong_ball.reset_speed:
        time_speed = BASE_SPEED
        pong_ball.reset_speed = False
        
    time.sleep(time_speed)
    
    pong_ball.move_ball(score_board = my_scoreboard)
    
    if (pong_ball.distance(paddle_one) < 50 and pong_ball.xcor() > 320) or (pong_ball.distance(paddle_two) < 45 and pong_ball.xcor() < -320):
        
        pong_ball.bounce_from_paddle(score_board = my_scoreboard)
        
        if time_speed > 0.01:
            time_speed -= 0.01

my_screen.exitonclick()


