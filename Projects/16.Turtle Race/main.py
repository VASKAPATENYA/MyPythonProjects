import turtle as t
import random as r
screen=t.Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
user_bet=screen.textinput("Make Your Bet!", prompt="Enter a color>> " )

colors=["yellow", "gray", "orange", "red", "blue", "green", "white"]
turtels=[]

def place_turtles():
    y=150
    for turtle_color in colors:
        tim=t.Turtle(shape="turtle")
        tim.clear()
        tim.color(turtle_color)
        tim.penup()
        tim.goto(x=-230, y=y)
        y-=50
        turtels.append(tim)

should_continue=True
place_turtles()
while should_continue:
    for i in range(len(turtels)):
        turtels[i].forward(r.randint(1,20))
        if turtels[i].xcor()>230:
            should_continue=False
            winner=turtels[i].fillcolor()
            if user_bet==winner:
                print("WELL DONE YOU WON!")
                play_again=screen.textinput("Play Again?", prompt="Y/N?")
                if play_again=="y":
                    turtels.clear()
                    place_turtles()
                    should_continue=True
            else:
                print(f"THE WINNER IS {winner.upper()} You Lost!")
                play_again=screen.textinput("Play Again?", prompt="Y/N?")
                if play_again=="y":
                    turtels.clear()
                    place_turtles()
                    should_continue=True
screen.exitonclick()