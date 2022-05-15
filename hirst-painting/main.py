import turtle
from turtle import Turtle, Screen
from random import choice

mc_mickay = Turtle()
mc_mickay.penup()
mc_mickay.hideturtle()
turtle.colormode(255)
# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 25)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
colors_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]
mc_mickay.setheading(225)
mc_mickay.forward(250)
mc_mickay.setheading(0)

for i in range(10):
    for j in range(10):
        mc_mickay.dot(20, choice(colors_list))
        mc_mickay.fd(50)
    if i%2==0:
        mc_mickay.left(90)
        mc_mickay.forward(50)
        mc_mickay.left(90)

    else:
        mc_mickay.right(90)
        mc_mickay.forward(50)
        mc_mickay.right(90)
    mc_mickay.forward(50)
screen = Screen()
screen.exitonclick()