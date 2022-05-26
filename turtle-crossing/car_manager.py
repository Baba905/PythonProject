from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []

    def create_car(self):
        chance = randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=0.5, stretch_len=2.5)
            car.color(choice(COLORS))
            car.setheading(180)
            car.penup()
            y = randint(-250, 250)
            car.goto(x=280, y=y)
            self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(MOVE_INCREMENT)

