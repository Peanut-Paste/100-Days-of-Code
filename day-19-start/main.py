from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = -120

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(-230, y)
    new_turtle.color(colors[turtle_index])
    y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
# def move_left():
#     tim.left(10)
# def move_right():
#     tim.right(10)
# def clear():
#     tim.reset()
# screen.listen()
# screen.onkeypress(move_forwards, "w")
# screen.onkeypress(move_backwards, "s")
# screen.onkeypress(move_left, "a")
# screen.onkeypress(move_right, "d")
# screen.onkeypress(clear, "c")

screen.exitonclick()