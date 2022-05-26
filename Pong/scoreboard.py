from turtle import Turtle


class ScoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        #self.write(arg=self.score, font=('Courier', 80, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=self.score, font=('Courier', 80, 'normal'))