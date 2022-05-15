from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        for i in range(3):
            self.snake_body.append(Turtle(shape="square"))
            self.snake_body[i].color("white")
            self.snake_body[i].penup()
            self.snake_body[i].goto(x=-i * 20, y=0)
        self.head = self.snake_body[0]
        self.head.color("blue")


    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_body_section(self):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_x = self.snake_body[-1].xcor()
        new_y = self.snake_body[-1].ycor()
        new_turtle.goto(x=new_x + 20, y=new_y)

        self.snake_body.append(new_turtle)
