from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed(5)

def move_forwards():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_counter_clockwise():
    tim.right(15)


def move_clockwise():
    tim.left(15)


def clean():
    tim.reset()



screen.listen()
screen.onkey(key="z", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clean)
screen.exitonclick()
