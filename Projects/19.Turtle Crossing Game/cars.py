import turtle
import random


class Cars:
    def __init__(self):
        self.all_cars=[]
        self.speed=10

    def create_cars(self):
        chance=random.randint(1,6)
        if chance==1:
            self.y=random.randint(-150,150)
            self.car=turtle.Turtle("square")
            self.car.penup()
            self.car.color("red")
            self.car.shapesize(stretch_len=1.5, stretch_wid=1)
            self.car.goto(x=340, y=self.y)
            self.all_cars.append(self.car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.speed)