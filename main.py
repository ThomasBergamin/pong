from turtle import Screen
from scoreboard import Scoreboard, screen_setup
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
scoreboard = Scoreboard()
BG_COLOR = "black"
TITLE = "Pong"
LEFT_PADDlE_UP = "z"
LEFT_PADDlE_DOWN = "s"
RIGHT_PADDLE_UP = "Up"
RIGHT_PADDLE_DOWN = "Down"
game_is_on = True

# Screen settings >
screen.setup(width=800, height=600)
screen.title(TITLE)
screen.bgcolor(BG_COLOR)
screen.tracer(0)
screen_setup()

# Creating paddles, positions as input >
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Shortcuts for the game
screen.listen()
screen.onkeypress(l_paddle.go_up, LEFT_PADDlE_UP)
screen.onkeypress(l_paddle.go_down, LEFT_PADDlE_DOWN)
screen.onkeypress(r_paddle.go_up, RIGHT_PADDLE_UP)
screen.onkeypress(r_paddle.go_down, RIGHT_PADDLE_DOWN)

ball = Ball()


while game_is_on:
    # Screen refresh
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detects collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # Detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()
