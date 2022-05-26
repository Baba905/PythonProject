from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=-30, y=270)
        self.hideturtle()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", font=('Arial', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", font=('Arial', 15, 'normal'))

    def reset_high_score(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                high_in_string = str(self.high_score)
                file.write(high_in_string)
        self.score = 0
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", font=('Arial', 15, 'normal'))

    """def game_over(self):
        self.goto(-30, 0)
        self.write(arg="Game Over", font=('Arial', 25, 'normal'))"""
