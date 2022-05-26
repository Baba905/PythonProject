import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=player.up)
game_is_on = True
while game_is_on:
    time.sleep(0.2/scoreboard.level)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Collision with turtle
    for car in car_manager.car_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Reach the other side

    if player.ycor() == 280:
        scoreboard.next_level()
        player.goto(STARTING_POSITION)
        print(f"You won the level{scoreboard.level}")


screen.exitonclick()