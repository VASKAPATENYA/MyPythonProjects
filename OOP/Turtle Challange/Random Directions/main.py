import turtle
import random
turtle.colormode(255)
my_screen=turtle.Screen()
my_screen.bgcolor("black")
ahmet=turtle.Turtle()
ahmet.shape("turtle")
ahmet.color("gray")
ahmet.pensize(10)
ahmet.speed(0)


directions=[0,90,180,270]

for i in range(1000000):
    ahmet.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    ahmet.setheading(directions[random.randint(0,3)])
    ahmet.forward(20)

my_screen.exitonclick()