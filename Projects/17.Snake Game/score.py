from asyncore import read
import turtle
class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("Projects\\17.Snake Game\\high_score.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("Projects\\17.Snake Game\\high_score.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
        self.goto(0,0)
        self.write("GAME OVER.", align="center", font=("Arial", 24, "normal"))
        self.score=0



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER.", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))