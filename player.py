from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        if self.ycor() < FINISH_LINE_Y:
            self.sety(self.ycor() + MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)