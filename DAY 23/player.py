from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.starting_position()
        
    def move_forward(self):
        if self.reached_finished_line() == False:
            self.sety(self.ycor() + MOVE_DISTANCE)

    def reached_finished_line(self):
        return self.ycor() >=  FINISH_LINE_Y

    def starting_position(self):
        self.goto(STARTING_POSITION)
