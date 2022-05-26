from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(x=-280, y=250)
        self.hideturtle()
        self.write(arg=f"Level : {self.level}", font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level : {self.level}", font=FONT)

    def game_over(self):
        self.goto(x=-50, y=0)
        self.write(arg="Game over", font=FONT)