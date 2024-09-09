from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(x=-10, y = 270)
        self.color("white")
        self.ht()
        self.score = 0
        self.high_score = int(self.get_high_score())
        self.display_score()
    
    def increment_score(self):
        self.score += 1
        self.display_score()
    
    def display_score(self):
        
        self.clear()
        self.setposition(x=-10, y = 270)
        self.write(str(f"Score: {self.score}"), align="center", font=('Courier', 15, 'normal'))
        
        self.setposition(x=-10, y = 250)
        self.write(str(f"High Score: {self.high_score}"), align="center", font=('Courier', 15, 'normal'))
    
    def game_over(self):
        self.goto(0,0)
        self.write(str(f"GAME OVER"), align="center", font=('Courier', 20, 'normal'))
        
    def reset_game(self):
        self.high_score = int(self.get_high_score())
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score(str(self.high_score))
                        
        self.score = 0
        self.display_score()
    
    def get_high_score(self):
        with open("high_score.txt", mode = "r") as high_score_file:
           return high_score_file.read()
        # return 0
    
    def set_high_score(self, high_score):
        with open("high_score.txt", mode = "w") as high_score_file:
            high_score_file.write(high_score)
    