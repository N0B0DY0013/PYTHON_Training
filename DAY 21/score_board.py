from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.setposition(x=-10, y = 270)
        self.color("white")
        self.ht()
        self.score = 0
        self.display_score()
    
    def increment_score(self):
        self.score += 1
        self.display_score()
    
    def display_score(self):
        self.clear()
        self.write(str(f"Score: {self.score}"), align="center", font=('Courier', 15, 'normal'))
    
    def game_over(self):
        self.goto(0,0)
        self.write(str(f"GAME OVER"), align="center", font=('Courier', 20, 'normal'))
    