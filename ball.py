from turtle import Turtle

# Parameters of the ball
BALL_INIT_POS = (0, 0)
BALL_COLOR = "white"
BALL_SHAPE = "circle"
BALL_SPEED = 15


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(BALL_INIT_POS)
        self.color(BALL_COLOR)
        self.shape(BALL_SHAPE)
        self.penup()
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()

