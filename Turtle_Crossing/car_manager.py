from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION_X = 300


class CarManager:
    def __init__(self):
        self.moving_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.setpos(STARTING_POSITION_X, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.moving_speed)

    def speedup(self):
        self.moving_speed += MOVE_INCREMENT
