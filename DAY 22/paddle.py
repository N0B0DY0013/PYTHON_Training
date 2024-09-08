
from turtle import Turtle

class Paddle(Turtle):
    
    TURTLE_PIXEL = 20
    
    def __init__(self, stretch_width, stretch_length, x_pos, y_pos, screen, paddle_color = "white" ):
        super().__init__()
        self.stretch_width = stretch_width
        self.stretch_length = stretch_length
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.paddle_color = paddle_color
        self.screen = screen
        self.penup()
        self.create_paddle()
        
    def create_paddle(self):
        self.shape("square")
        self.color(self.paddle_color)
        self.resizemode("user")
        self.shapesize(stretch_wid = self.stretch_width, stretch_len = self.stretch_length)
        self.goto(x = self.x_pos, y = self.y_pos)
        
        
    def move_up(self):
        if self.ycor() < ( (self.screen.window_height() / 2) - self.TURTLE_PIXEL * 2):
            self.goto(x = self.xcor(), y = self.ycor() + self.TURTLE_PIXEL)
            self.screen.update()
        
    def move_down(self):
        if ( self.ycor() + (self.stretch_width * -self.TURTLE_PIXEL) ) > ( -(self.screen.window_height() / 2) + (-self.TURTLE_PIXEL * 2) ):
            self.goto(x = self.xcor(), y = self.ycor() - self.TURTLE_PIXEL)
            self.screen.update()