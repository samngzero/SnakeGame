from turtle import Turtle

class ScoreBoad(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", False, "center", ("Arial", 16, "normal"))

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", False, "center", ("Arial", 40, "normal"))

    def add_score(self):
        self.score+=1
        self.clear()
        self.update()

