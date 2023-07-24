from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snakes()
        self.head = self.segments[0]

    def create_snakes(self):
        for position in COORDINATES:
            self.new_segment(position)

    def new_segment(self, position):
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.setpos(position)
        self.segments.append(new_seg)

    def add_segment(self):
        self.new_segment(self.segments[-1].position())

    def move(self):
        for segment_no in range(len(self.segments) - 1, 0, -1):
            self.segments[segment_no].goto(self.segments[segment_no - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

