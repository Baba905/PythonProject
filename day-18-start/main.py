import turtle
from turtle import Turtle, Screen
import  random
mc_mickay= Turtle()
turtle.colormode(255)
#mc_mickay.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# for i in range(3,11):
#     mc_mickay.color(random.choice(colours))
#     for j in range(i):
#         mc_mickay.forward(100)
#         mc_mickay.left(360/i)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

# mc_mickay.pensize(5)
mc_mickay.speed(20)
# for i in range(200):
#     mc_mickay.pencolor(random_color())
#     direction = random.randint(1,4)
#     mc_mickay.forward(20)
#     if direction==1:
#         mc_mickay.left(90)
#     elif direction==2:
#         mc_mickay.right(90)
#     elif direction==3:
#         mc_mickay.right(180)
#     else:
#         mc_mickay.right(180)

for _ in range(100):
    mc_mickay.pencolor(random_color())
    mc_mickay.circle(100)
    mc_mickay.setheading(mc_mickay.heading()+10)






screen = Screen()
screen.exitonclick()