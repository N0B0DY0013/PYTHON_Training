from turtle import Turtle


class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_one_score = 0
        self.player_two_score = 0
        self.show_score()
    
    def show_score(self):
        self.clear()
        
        self.goto(x = 200, y = 200)
        self.write(self.player_one_score, align = "center", font = ("Courier", 70, "normal"))
        
        self.goto(x = -200, y = 200)
        self.write(self.player_two_score, align = "center", font = ("Courier", 70, "normal"))
        