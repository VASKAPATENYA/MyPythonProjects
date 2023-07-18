import turtle

class Line:
    def __init__(self) -> None:
        self.y=280
        self.create_line()

    def create_line(self):
        while self.y>-300:
            line=turtle.Turtle("square")
            line.penup()
            line.shapesize(1,0.2, 1) 
            line.color("white")
            line.goto(x=0, y=self.y)
            self.y-=35

