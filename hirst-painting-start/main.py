# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     rgb = (red, green, blue)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)
import turtle
import turtle as t
import random
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()

def hirst_painting(dot_x, dot_y):
    y = -229.81
    for b in range(dot_y):
        x = -229.81
        for i in range(dot_x):
            tim.goto(x, y)
            tim.dot(20, random.choice(color_list))
            x += 50
        y += 50

hirst_painting(10, 10)

screen = t.Screen()
screen.exitonclick()