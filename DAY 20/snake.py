from turtle import Turtle

class Snake():
    
    def __init__(self) -> None:
        self.pixel = 20
        self.snake_blocks = []
        self.create_starting_snake()
        
    def create_starting_snake(self):
        for i in range(0, 3):
            self.snake_blocks.append(Turtle())
            self.snake_blocks[i].penup()
            self.snake_blocks[i].shape("square")
            self.snake_blocks[i].color("white")
            self.snake_blocks[i].setpos(x = (-i * self.pixel), y = 0)

        
    def move_snake(self, direction):
        
        for i in range(len(self.snake_blocks) - 1, 0, -1):
            self.snake_blocks[i].setposition(self.snake_blocks[i - 1].position())
        
        
        if direction == "up":    
            if self.snake_blocks[0].heading() != 270:
                self.snake_blocks[0].seth(90)
        elif direction == "down":
            if self.snake_blocks[0].heading() != 90:
                self.snake_blocks[0].seth(270)
        elif direction == "left":
            if self.snake_blocks[0].heading() != 0:
                self.snake_blocks[0].seth(180)
        elif direction == "right":
            if self.snake_blocks[0].heading() != 180:
                self.snake_blocks[0].seth(0)
        
        self.snake_blocks[0].forward(self.pixel)
        
    def hit_horizontal_edge(self, screen_width):
        return ((self.snake_blocks[0].xcor() + self.snake_blocks[0].width()) >= ((screen_width / 2))) or ((self.snake_blocks[0].xcor() + self.snake_blocks[0].width()) <= (-(screen_width / 2)))

    def hit_vertical_edge(self, screen_height):
        return ((self.snake_blocks[0].ycor() + self.snake_blocks[0].width()) >= ((screen_height / 2) + self.pixel)) or ((self.snake_blocks[0].ycor() + self.snake_blocks[0].width()) <= (-((screen_height / 2) - self.pixel )))
            