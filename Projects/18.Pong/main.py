# region Imports

from email.mime import audio
from turtle import Screen, Turtle
from players import Players
from ball import Ball
from line import Line
from scoreboard import Score
from players import Players
import time

# endregion

# region Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

# endregion

# region Line

line=Line()

# endregion

# region Score

score=Score()

# endregion

# region Players

player1 = Players((350, 0))
player2 = Players((-350,0))

# endregion

# region Ball

ball = Ball()

# endregion

# region Key Controls

screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")
screen.onkey(player2.go_up, "w")
screen.onkey(player2.go_down, "s")

# endregion

# region Hub

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor()<-380:
        ball.reset_position()
        score.plyr1_point()
    
    if ball.xcor()>380:
        ball.reset_position()
        score.plyr2_point()

        
screen.exitonclick()

# endregion