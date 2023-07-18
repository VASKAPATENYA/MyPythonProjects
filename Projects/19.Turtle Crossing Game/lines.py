from turtle import Turtle

class Lines:
    def __init__(self):
        self.x=320
        self.y=100
        for _ in range(3):
            for i in range(8):
                self.line=Turtle("square")
                self.line.color("white")
                self.line.penup()
                self.line.shapesize(stretch_wid=0.2, stretch_len=3)
                self.line.goto(x=self.x, y=self.y)
                self.x-=90
            self.y-=100
            self.x=320