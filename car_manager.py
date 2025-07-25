from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-230, 250)
            new_car.goto(310, random_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
        