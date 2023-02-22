from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# silly little bits of data
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

# create game loop
is_on = True
while is_on:
    screen.update()
    time.sleep(0.04)
    snake.move()    

    # detect collision with food and update score
    if snake.head.distance(food) < 12:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    
    # detect collision with wall
    shx = snake.head.xcor()
    shy = snake.head.ycor()
    if shx > 290 or shx < -295 or shy > 295 or shy < -290:
        # score resets
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for s in snake.my_snake[1:]:
        if snake.head.distance(s) < 2:
            scoreboard.reset()
            snake.reset()
            
screen.exitonclick()