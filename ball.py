from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(.5, .5, 5)
        self.goto(0,0)
        self.color("white")
        self.penup()
        self.angle = 30
        self.speed = .4

    def movef(self):
        self.setheading(self.angle)
        self.forward(self.speed)

    def reset(self):
        self.goto(0,0)


