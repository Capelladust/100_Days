from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-200, 270)
        self.score_one = 0
        self.score_two = 0

    def player_one(self):
        self.goto(-200, 270)
        self.write(f"Score: {self.score_one}", True, align=ALIGNMENT, font=FONT)

    def player_two(self):
        self.goto(200, 270)
        self.write(f"Score: {self.score_two}", True, align=ALIGNMENT, font=FONT)

    def player_one_add(self):
        self.goto(-200, 270)
        self.score_one += 1
        self.clear()
        self.player_one()

    def player_two_add(self):
        self.goto(200, 270)
        self.score_two += 1
        self.clear()
        self.player_two()






