from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.shape("square")
        self.shapesize(stretch_wid = 1, stretch_len = 2)   
        self.renew_car(x_pos = random.randint(-280, 280), y_pos = random.randint(-240, 280)) 

    def renew_car(self, x_pos, y_pos):
        self.setx(x_pos)
        self.sety(y_pos)
        self.color(random.choice(COLORS))
        
    def move_left(self, level):
        if self.xcor() > -320:
            self.setx(self.xcor() + -(self.move_speed + (MOVE_INCREMENT * (level - 1))))
        else:
            self.renew_car(x_pos = 300, y_pos = random.randint(-240, 280))