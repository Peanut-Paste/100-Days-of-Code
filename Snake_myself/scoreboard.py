from turtle import Turtle

Y_POSITION = 270
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')
COLOR = "white"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.setpos(0, Y_POSITION)
        self.color(COLOR)
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

