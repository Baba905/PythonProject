from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color: ")
color = ["red", "green", "purple", "blue", "orange", "yellow"]

turtles = []
for i in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].speed(6)
    turtles[i].color(color[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=100 - i * 50)
if user_bet:
    is_race_on = True

while is_race_on:

    for i in range(6):
        if turtles[i].xcor() < 230:
            turtles[i].forward(randint(0, 10))
        else:
            is_race_on = False
            if turtles[i].pencolor()== user_bet:
                print(f"You won the game, the {user_bet} is winner!")
            else:
                print(f"You lose the game, the {turtles[i].pencolor()} is winner!")
screen.exitonclick()
