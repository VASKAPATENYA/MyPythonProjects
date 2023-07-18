import turtle
import random
turtle.colormode(255)
my_screen=turtle.Screen()
my_screen.bgcolor("gray")
ahmet=turtle.Turtle()
ahmet.shape("turtle")
ahmet.color("black")
ahmet.pencolor("black")
ahmet.speed(0)

for i in range(37):
    ahmet.circle(100)
    ahmet.setheading(ahmet.heading() + 10)

my_screen.exitonclick()