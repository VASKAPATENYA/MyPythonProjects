import turtle

class Level:
    def __init__(self) -> None:
        self.score=1
        self.level=turtle.Turtle()
        self.level.goto(x=-290, y=180)
        self.level.hideturtle()
        self.level.color("white")
        self.level.penup()
        self.level.write(f"Level: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increse_level(self):
        self.level.clear()
        self.score+=1
        self.level.write(f"Level: {self.score}", align="center", font=("Arial", 24, "normal"))
