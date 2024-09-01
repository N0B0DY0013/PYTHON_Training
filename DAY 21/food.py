
from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("lawngreen")
        self.shapesize(stretch_wid = 0.75, stretch_len = 0.75)
        self.setheading(90)
        self.speed("fastest")
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
    
    
    def move_food(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))