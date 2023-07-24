import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(50)
#         tim.right(angle)

# for shape in range(3, 11):
#     tim.color((random.random(),random.random(),random.random()))
#     draw_shape(shape)

# def direction():
#     list = [0, 90, 180, 270]
#     tim.forward(30)
#     tim.setheading(random.choice(list))


# for i in range(1000):
#     tim.color(random_color())
#     direction()

tim.speed("fastest")
# tim.pensize(2)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r,g,b)
    return rgb

shift = 3

def draw_spirograph(size_of_gra):
    for i in range(int(360/size_of_gra)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gra)

draw_spirograph(1)

screen = Screen()
screen.exitonclick()
