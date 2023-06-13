from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
start_x = -40
snake = Snake()
# food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True
while is_on:
    food = Food()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increament_score()

        elif snake.head.xcor() > 300:
            score.reset()
            snake.reset()

        elif snake.head.ycor() > 300:
            score.reset()
            snake.reset()
        elif snake.head.xcor() < -300:
            score.reset()
            snake.reset()
        elif snake.head.ycor() < -300:
            score.reset()
            snake.reset()

        for segments in snake.segments[1:]:
            if segments == snake.head:
                pass
            elif snake.head.distance(segments) < 10:
                score.reset()
                snake.reset()


screen.exitonclick()
