from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-260, 260), random.randint(-260, 260))
