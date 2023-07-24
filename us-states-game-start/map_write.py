from turtle import Turtle

FONT = ("Arial", 8, "normal")
ALIGN = "center"


class MapWrite():
    def __init__(self):
        self.tim = Turtle()
        self.tim.penup()
        self.tim.hideturtle()

    def write(self, text, x, y):
        self.tim.goto(x, y)
        self.tim.write(text, align=ALIGN, font=FONT)
