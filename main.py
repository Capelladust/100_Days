from turtle import Turtle, Screen
from paddly import Pong
from ball import Ball
from game_over import Game
from scoreboard import Score
import random


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)

player_one = Pong((350, 0))
player_two = Pong((-350, 0))

ball = Ball()
over = Game()
total = Score()




screen.listen()
screen.onkey(player_one.go_up, "Up")
screen.onkey(player_one.go_down, "Down")
screen.onkey(player_two.go_up, "w")
screen.onkey(player_two.go_down, "s")

game = True

total.player_one()
total.player_two()

while game:
    screen.update()
    ball.movef()

    if player_one.distance(ball) < 40:
         ball.angle = random.randint(-210, -150)
         ball.speed = ball.speed + .01

    if player_two.distance(ball) < 40:
        ball.angle = random.randint(30, 75)
        ball.speed = ball.speed + .01

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.angle = ball.angle * -1

    if ball.xcor() > 390:
        total.player_one_add()
        total.player_two()
        ball.reset()
        ball.angle = 210
        ball.speed = .4
        over.restart()
        print(total.score_one)
    elif ball.xcor() < -390:
        total.player_two_add()
        total.player_one()
        ball.reset()
        ball.angle = 30
        ball.speed = .4
        over.restart()


    if total.score_one == 10 or total.score_two == 10:
        over.end()
        game = False












screen.exitonclick()