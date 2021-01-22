from turtle import Turtle

# Parameters of the paddle
PADDLE_SPEED = 20
PADDLE_COLOR = "white"


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(self.position)

    def go_up(self):
        new_y = self.ycor() + PADDLE_SPEED
        self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - PADDLE_SPEED
        self.sety(new_y)


