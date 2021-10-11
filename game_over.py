from turtle import Turtle


class Game(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,0)
        self.penup()
        self.color("white")
        self.isvisible()

    def end(self):
        self.write("GAME OVER... THANKS FOR PLAYING!", align="center", font=("Arial", 36, "normal"))

    def restart(self):
        self.hideturtle()