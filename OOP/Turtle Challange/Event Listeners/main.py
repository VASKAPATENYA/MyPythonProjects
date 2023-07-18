import turtle as t

screen=t.Screen()
screen.bgcolor("gray")
tim =t.Turtle()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_right():
    new_heading=tim.heading() + 10
    tim.setheading(new_heading)

def move_left():
    new_heading=tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    screen.bgcolor("gray")
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_right)
screen.onkey(key="c", fun=clear)



screen.exitonclick()