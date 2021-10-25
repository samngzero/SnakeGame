from turtle import Turtle
from random import randint

import food

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.turtlesize(0.5)
        self.penup()
        self.respawn()

    def respawn(self):
        self.goto(20 * randint(-13, 13), 20 * randint(-13, 13))

