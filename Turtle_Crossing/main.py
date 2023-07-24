from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    if player.ycor() >= 280:
        player.refresh()
        scoreboard.level_up()
        car_manager.speedup()

    for car in car_manager.all_cars:
        if player.distance(car.position()) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
