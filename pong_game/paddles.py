from turtle import Turtle

COLOR = "white"
SHAPE = "square"
SIZE = {
    "width": 5,
    "height": 1
}
UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddles(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.color(COLOR)
        self.shapesize(stretch_wid=SIZE["width"], stretch_len=SIZE["height"])
        self.setpos(position)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


