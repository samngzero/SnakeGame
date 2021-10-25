import time
from turtle import Screen, Turtle
from snake import SnakeBody
from food import Food
from scoreboard import ScoreBoad

screen_size=600

screen = Screen()
screen.setup(screen_size, screen_size)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = SnakeBody()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_on = True

food = Food()
score = ScoreBoad()

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #scoring
    if snake.body[0].distance(food.xcor(),food.ycor())<10:
        food.respawn()
        snake.extend()
        score.add_score()
    #wall
    if abs(snake.body[0].xcor())>screen_size/2-20 or abs(snake.body[0].ycor())>screen_size/2-20:
        score.gameover()
        game_on=False

    #tail
    for i in snake.body[1:]:
        if snake.body[0].distance(i)<10:
            score.gameover()
            game_on = False



screen.exitonclick()
