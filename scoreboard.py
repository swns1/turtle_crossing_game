from turtle import Turtle

with open("C:\\Python-Workspace\\Python\\turtle-crossing-start\\data.txt") as f:
    score = f.read()
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.highscore = int(score)
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-150, 250)
        self.write(f"Level: {self.level}   High Score: {self.highscore}" , align="center", font=('Courier', 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=('Courier', 25, 'normal'))
        if self.level > self.highscore:
            self.highscore = self.level
            with open("C:\\Python-Workspace\\Python\\turtle-crossing-start\\data.txt", mode="w") as f:
                f.write(str(self.highscore))

    def add_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}   High Score: {self.highscore}", align="center", font=('Courier', 15, 'normal'))