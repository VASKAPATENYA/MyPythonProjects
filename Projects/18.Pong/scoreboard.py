from tkinter import CENTER
from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1=0
        self.player2=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.player2, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.player1, align="center", font=("Arial", 80, "normal"))

    def plyr1_point(self):
        self.player1+=1
        self.update_score()
    
    def plyr2_point(self):
        self.player2+=1
        self.update_score()