from turtle import Turtle, Screen
import time
import snake

my_screen = Screen()
TURTLE_PIXEL = 20


def main():
    my_screen.setup(width=600, height=600)
    my_screen.bgcolor("black")
    
    my_screen.tracer(0)
    
    my_snake = snake.Snake()
    my_screen.update()


    my_screen.listen()
    
    my_screen.onkeypress(lambda: my_snake.move_snake("up"), "w")
    my_screen.onkeypress(lambda: my_snake.move_snake("up"), "Up")
    
    my_screen.onkeypress(lambda: my_snake.move_snake("left"), "a")
    my_screen.onkeypress(lambda: my_snake.move_snake("left"), "Left")
    
    my_screen.onkeypress(lambda: my_snake.move_snake("down"), "s")
    my_screen.onkeypress(lambda: my_snake.move_snake("down"), "Down")
    
    my_screen.onkeypress(lambda: my_snake.move_snake("right"), "d")
    my_screen.onkeypress(lambda: my_snake.move_snake("right"), "Right")
    
    not_game_over = True
    while not_game_over:
        my_screen.update()
        time.sleep(0.05)
        
        my_snake.move_snake("forward")
        
        if my_snake.hit_horizontal_edge(my_screen.window_width()) or my_snake.hit_vertical_edge(my_screen.window_height()):
            not_game_over = False
        
    my_screen.exitonclick()
    
main()