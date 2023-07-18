from ctypes.wintypes import RGB
import turtle
import random

turtle.colormode(255)


ahmet=turtle.Turtle()
ahmet.shape("turtle")
ahmet.color("gray")
my_screen=turtle.Screen()
ahmet.speed(0)

my_screen.bgcolor("black")
sides_of_the_shapes=3

while sides_of_the_shapes<361:
    ahmet.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    for i in range(sides_of_the_shapes):
        ahmet.forward(30)
        ahmet.right(360/sides_of_the_shapes)
    sides_of_the_shapes+=1






my_screen.exitonclick()