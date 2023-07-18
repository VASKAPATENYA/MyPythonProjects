from secrets import choice
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on=True


money_machine=MoneyMachine()
coffe_maker=CoffeeMaker()
menu=Menu()


while is_on:
    options=menu.get_items()
    chosen_coffee=input(f"What would you like? ({options})>>> ")
    if chosen_coffee=="off":
        is_on=False
    elif chosen_coffee=="report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(chosen_coffee)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)