from turtle import Turtle, Screen

class SnakeBody():

    def __init__(self):
        self.body = []
        self.sp = 6
        self.travel = 20
        self.crate_snake()

    def crate_snake(self):
        for i in range(3):
            self.add_body((-i * 20,0))

    def add_body(self,pos):
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.speed(self.sp)
        new_snake.setposition(pos)
        new_snake.fillcolor("white")
        self.body.append(new_snake)

    def extend(self):
        self.add_body(self.body[-1].position())

    def follow(self):
        l = len(self.body)
        for i in range(l - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].xcor(), self.body[i - 1].ycor())

    def move(self):
        self.follow()
        self.body[0].fd(self.travel)

    def turn_up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def turn_down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def turn_right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def turn_left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def reset(self):
        self.clear()

