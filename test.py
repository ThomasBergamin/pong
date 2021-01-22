from turtle import Screen, Turtle
from scoreboard import Scoreboard, screen_setup
from paddle import Paddle
import time

screen = Screen()
scoreboard = Scoreboard
BG_COLOR = "black"
TITLE = "Pong"
game_is_on = True


# Screen settings >
screen.setup(width=1000, height=600)
screen.title(TITLE)
screen.bgcolor(BG_COLOR)
screen.tracer(1)

turtle = Turtle()
turtle.shape("square")
turtle.color("white")
turtle.setheading(-90)
turtle.shapesize(stretch_len=5)

#screen.listen()
#screen.onkey(paddle.up, "Up")
#screen.onkey(paddle.down, "Down")
#screen.onkey(paddle.left, "z")
#screen.onkey(paddle.right, "s")





screen.exitonclick()
