from os import stat
import turtle
import pandas

# region Screen

screen=turtle.Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

# endregion


# region States

data=pandas.read_csv("50_states.csv")
state_names=data["state"].tolist()

# endregion


# region Input 
is_game_on=True
score=0
state_row_number=0
ccc=0
while is_game_on:
    if score<50:
        guess=turtle.textinput(f"{score}/50 Correct", "What's another state name?")
        for state in state_names:
            if guess==state:
                tim=turtle.Turtle()
                tim.color("black")
                tim.penup()
                tim.hideturtle()
                a=data[data["state"]==state]
                new_x=int(a["x"])
                b=data[data["state"]==state]
                new_y=int(b["y"])
                tim.goto(x=new_x, y=new_y)
                tim.write(state, align="center", font=("Arial", 12, "bold"))
                score+=1
                state_names.remove(state)
            elif guess=="Exit":
                missed_states=pandas.DataFrame(state_names)
                missed_states.to_csv("Missed States.csv")
                break
            state_row_number+=1
    else:
       tim=turtle.Turtle()
       tim.color("black")
       tim.hideturtle()
       tim.penup()
       tim.write("Well Done You've Finished The Game!", align="center", font=("Arial", 30, "bold"))


# endregion



turtle.mainloop()
screen.exitonclick()