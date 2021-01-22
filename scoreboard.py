from turtle import Turtle

START_POSITION = (0, -285)
LINES_COLOR = "white"
LINES_SIZE = 3
LINES_LENGTH = 30
LINES_GAP = 20
NUMBER_LINES = 20


def screen_setup():
    turtle = Turtle()
    turtle.color("white")
    turtle.penup()
    turtle.goto(START_POSITION)
    turtle.pencolor(LINES_COLOR)
    turtle.pensize(LINES_SIZE)
    turtle.speed("fastest")

    for _ in range(NUMBER_LINES):
        turtle.pendown()
        turtle.setheading(90)
        turtle.forward(LINES_LENGTH)
        turtle.penup()
        turtle.forward(LINES_GAP)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()