import time
from turtle import Turtle


class ScoreBoad(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.highestscore = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}    Highest Score: {self.highestscore}", False, "center",
                   ("Arial", 16, "normal"))

    def highest_score(self):
        if self.highestscore < self.score:
            self.highestscore = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.highestscore}")
        self.score = 0

    def print_gameover(self):
        self.update()
        self.goto(0, 0)
        self.write("Game Over", False, "center", ("Arial", 40, "normal"))

    def gameover(self):
        self.highest_score()
        self.print_gameover()

    def restart(self):
        for i in range(3):
            self.print_gameover()
            self.goto(0, -20)
            self.write(f"Restart in: {3 - i}", False, "center", ("Arial", 20, "normal"))
            time.sleep(1)

    def add_score(self):
        self.score += 1
        self.update()
