import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

"""
figure out how the moving cars is created
how to move it
create a turtle that moves up
create a score board
when the turtle reach the top it restart and the car moves faster
update the score 
game over if the cars hit the turtle
"""

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
car_manager = CarManager()
level = Scoreboard()


screen.onkeypress(key="w", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.cars:
        if player.distance(car) < 25:
            level.game_over()
            game_is_on = False

    if player.ycor() == 280:
        level.add_level()
        player.reset()
        car_manager.increase_speed()
    
screen.exitonclick()