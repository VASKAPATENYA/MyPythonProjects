from turtle import Turtle

class Player:
    def __init__(self) -> None:
        self.turtle=Turtle("turtle")
        self.turtle.penup()
        self.turtle.color("green")
        self.turtle.shapesize(stretch_len=1, stretch_wid=1)
        self.turtle.seth(90)
        self.turtle.goto(x=0, y=-200)
    
    def up(self):
        self.turtle.forward(10)

    def game_over(self):
        write_game_over=Turtle()
        write_game_over.penup()
        write_game_over.color("white")
        write_game_over.hideturtle()
        write_game_over.goto(-100, 0)
        write_game_over.write("Game Over.", font=("Arial", 30, "normal") )

    def win(self):
        self.turtle.goto(x=0, y=-200)