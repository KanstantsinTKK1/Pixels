import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
import colorgram


# list_colors = colorgram.extract('hirst_spot_painting.jpg', 30)
#
# print(list_colors)
# new_list = []
# for item in list_colors:
#     new_tuple = (item.rgb.r, item.rgb.g, item.rgb.b)
#     new_list.append(new_tuple)
#
# print(new_list)

Jerry = Turtle()
Jerry.ht()
Jerry.speed(0)
Jerry.penup()
Jerry.teleport(-230, -200)
colors = [(239, 221, 114), (18, 111, 194), (223, 60, 94), (235, 150, 75), (143, 88, 49), (115, 147, 210), (211, 127, 164), (34, 194, 117), (139, 183, 19), (190, 17, 39), (107, 105, 195), (232, 55, 45), (244, 147, 183), (113, 191, 149), (190, 47, 68), (18, 187, 208), (44, 52, 106), (135, 220, 240), (146, 229, 169), (206, 210, 6), (21, 152, 117), (237, 172, 154), (108, 43, 41), (32, 42, 75), (181, 177, 221), (75, 38, 33)]


def pixels (number):
    up_step = -200
    for ver_num in range(number):
        for hor_num in range(number):
            Jerry.dot(20,random.choice(colors))
            if hor_num != number - 1:
                Jerry.forward(50)
        up_step += 50
        Jerry.teleport(-230, up_step)

pixels(10)

screen = Screen()
screen.exitonclick()