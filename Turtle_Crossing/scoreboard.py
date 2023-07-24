from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.setpos(-280, 240)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def level_up(self):
        self.level += 1
        self.refresh()

    def game_over(self):
        self.setpos(0, 0)
        self.write("Game Over", align="center",font=FONT)