from turtle import Turtle

FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    
    def __init__(self, level, car_count):
        super().__init__()
        self.level = level
        self.car_count = car_count
        self.penup()
        self.hideturtle()
        self.update_level()
        
    def update_level(self):
        self.clear()
        self.goto(x = -290, y = 270)
        self.write(f"Level: {self.level}", align = "left", font = FONT)
        self.goto(x = -290, y = 250)
        self.write(f"Car Count: {self.car_count}", align = "left", font = FONT)
 

    def game_over(self):
        self.goto(x = 0, y = 0)
        self.write(f"GAME OVER", align = "center", font = ("Courier", 24, "normal"))