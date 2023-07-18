import turtle

ahmet=turtle.Turtle()
ahmet.shape("turtle")
ahmet.color("red")
ahmet.position()
for i in range(20):
    ahmet.forward(5)
    ahmet.penup()
    ahmet.forward(5)
    ahmet.pendown()
# ahmet.forward(100)
# ahmet.right(90)
# ahmet.forward(100)
# ahmet.right(90)
# ahmet.forward(100)
# ahmet.right(90)
# ahmet.forward(100)


my_screen=turtle.Screen()
my_screen.exitonclick()

# from re import L
# import prettytable

# table=prettytable.PrettyTable()
# table.align="c"
# table.field_names=["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtel", "Water"])
# table.add_row(["Charmander", "Fire"])
# print(table)