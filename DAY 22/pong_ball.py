
from turtle import Turtle
import random


class PongBall(Turtle):
    
    def __init__(self, x_pos, y_pos, screen):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.reset_speed = False
        self.create_ball()
        
    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.goto(x = self.x_pos, y = self.y_pos)
        
    def move_ball(self, score_board):
        
        # checks if it reaches beyond vertical screen (top/bottom)
        if self.ycor() >= ( (self.screen.window_height() / 2) - 15 ) or self.ycor() <= -( (self.screen.window_height() / 2) - 15):
            self.y_move *= -1

        # checks if it reaches beyond horizontal screen (right)
        if self.xcor() >= ( (self.screen.window_width() / 2) - 15 ):
            score_board.player_two_score += 1
            score_board.show_score()
            self.x_move *= random.choice([1, -1])
            self.goto(x = 0, y = -280)
            self.reset_speed = True
        
        # checks if it reaches beyond horizontal screen (left)
        if self.xcor() <= -( (self.screen.window_width() / 2) - 15):
            score_board.player_one_score += 1
            score_board.show_score()
            self.x_move *= random.choice([1, -1])
            self.goto(x = 0, y = -280)
            self.reset_speed = True
            
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        
        self.screen.update()
        
    def bounce_from_paddle(self, score_board):
        self.x_move *= -1
        self.move_ball(score_board)