from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=-30, y=270)
        self.hideturtle()
        self.write(arg=f"Score: {self.score}", font=('Arial', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(-30, 0)
        self.write(arg="Game Over", font=('Arial', 25, 'normal'))