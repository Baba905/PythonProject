from turtle import Screen
from paddle import Paddle
from player import Player
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

robot = Paddle()
player = Player()
ball = Ball()
p_score = ScoreBoard()
r_score = ScoreBoard()

screen.onkey(key="Up", fun=player.up)
screen.onkey(key="Down", fun=player.down)

robot.goto(x=-350, y=0)
player.goto(x=350, y=0)
p_score.goto(x=100, y=200)
r_score.goto(x=-100, y=200)

robot.speed("fastest")
while True:
    screen.update()
    time.sleep(0.1)
    robot.forward(20)
    ball.move()

    if robot.distance(x=-350, y=270) == 10:
        robot.setheading(270)
        print("Work for south")
    elif robot.distance(x=-350, y=-270) == 10:
        robot.setheading(90)
        print("Work for north")

    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Ball collision with paddle
    if ball.distance(player) < 50 and ball.xcor() > 330:
        ball.bounce_x()
        print("Touch player")
    elif ball.distance(robot) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        print("Touch robot")

    # Player miss ball
    if ball.xcor() > 380:
        ball.reset_position()
        r_score.increase_score()

    # Robot miss ball
    if ball.xcor() < -380:
        ball.reset_position()
        p_score.increase_score()

screen.exitonclick()
