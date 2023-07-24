from turtle import Turtle
import random

COLOR = "white"
SHAPE = "circle"
MOVE_DISTANCE = 10
SPEED = "slowest"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.speed(SPEED)
        self.penup()
        self.color(COLOR)
        self.setheading(random.randint(0, 360))
        self.move_d_x = 10
        self.move_d_y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.move_d_x
        new_y = self.ycor() + self.move_d_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_d_y *= -1

    def bounce_x(self):
        self.move_d_x *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



