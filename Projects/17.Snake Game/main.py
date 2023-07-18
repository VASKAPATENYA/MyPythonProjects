import turtle as t
from time import sleep
from snake import Snake
from food import Food
from score import Score


# Screen Features
screen=t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("SNAKE")
screen.tracer(0)
screen.listen()

# Create The Snake
snake=Snake()

# Creating The Food
food=Food()

# Creating The Score
score=Score()

# Controlling The Snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on=True
while game_is_on:
    screen.update()
    sleep(0.1)

    # Move The Snake
    snake.move_snake()

    # Detecting Collision With The Food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() < 300 and snake.head.xcor() > -300 and snake.head.ycor() < 300 and snake.head.ycor() > -300:
       pass
    else:
        score.reset_score()
        game_is_on=False


    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            score.reset_score()
            game_is_on=False



screen.exitonclick()
