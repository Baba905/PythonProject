from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game ")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()

game_is_on = True

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        snake.add_body_section()
        score.increase_score()
        food.refresh()
    # Collision with wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        score.reset_high_score()
        snake.reset()
    # Collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_high_score()
            snake.reset()

screen.exitonclick()
