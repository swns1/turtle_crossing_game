from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-240, 250)
        self.write(f"Level: {self.level}", align="center", font=('Courier', 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=('Courier', 25, 'normal'))

    def add_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=('Courier', 15, 'normal'))