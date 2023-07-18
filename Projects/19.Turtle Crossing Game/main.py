import time
import turtle as t
from lines import Lines
from cars import Cars
from player import Player
from level import Level

# region Screen

screen=t.Screen()
screen.title("Cross Over")
screen.bgcolor("black")
screen.setup(width=700, height=450)
screen.tracer(0)
screen.listen()

# endregion


# region Lines

lines=Lines()

# endregion


# region Cars

# screen.tracer(1)
cars=Cars()

# endregion


# region Player

player=Player()

screen.onkey(player.up, "Up")

# endregion


# region Level

level=Level()

# endregion

is_game_on=True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()
    if player.turtle.ycor()>200:
        player.win()
        cars.speed+=5
        level.increse_level()
    for i in cars.all_cars:
        if player.turtle.distance(i)<30:
            player.game_over()
            is_game_on=False
    


screen.exitonclick()