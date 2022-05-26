from paddle import Paddle
UP = 90
DOWN = 270


class Player(Paddle):
    def __init__(self):
        super().__init__()
        self.speed("fast")

    def up(self):
        self.setheading(UP)
        if self.ycor() == 270:
            self.forward(0)
        self.forward(20)

    def down(self):
        self.setheading(DOWN)
        if self.ycor() == -270:
            self.forward(0)
        self.forward(20)
        