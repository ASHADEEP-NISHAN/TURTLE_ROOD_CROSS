from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.goto(-200,260)
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"LEVEL {self.level}", move=False, align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.show_level()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME-OVER", move=False, align="center", font=FONT)
