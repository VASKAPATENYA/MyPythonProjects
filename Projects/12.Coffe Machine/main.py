#region MENU
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#endregion

from art import logo
import os
os.system('cls')
print(logo)

# Variables
should_continue=True
water= 500
milk= 500
coffee= 500
total_money=0
money_values={"quarters": 0.25,"dimes": 0.10,"pennies": 0.01,"nickels": 0.05}
can_make=True

while should_continue:
    #TODO 1>> Input("What would you like? espresso/latte/cappucino")


    first_input=input("What would you like? espresso/latte/cappucino>>> ")


    #TODO 2>>Turn off the machine by typing "off"

    if first_input=="off":
        os.system('cls')
        print(logo)
        print("Thanks For Everything!")
        should_continue=False
        can_make=False


    #TODO 3>> Print report

    if first_input=="report":
        print(f"Water : {water}ml")
        print(f"Milk  : {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Total Money : ${total_money}")
        first_input=input("What would you like? espresso/latte/cappucino>>> ")


    #TODO 4>> Check if the resources are sufficient

    #Espresso
    if first_input=="espresso":
        if water >= MENU["espresso"]["ingredients"]["water"] and coffee >= MENU["espresso"]["ingredients"]["coffee"]:
            print("I can make you an espresso")
        else:
            print("I can't make you an espresso")
            can_make=False

    #Latte
    if first_input=="latte":
        if water >= MENU["latte"]["ingredients"]["water"] and coffee >= MENU["latte"]["ingredients"]["coffee"] and milk >= MENU["latte"]["ingredients"]["milk"]:
            print("I can make you a latte")
        else:
            print("I can't make you a latte")
            can_make=False

    #Cappucino
    if first_input=="cappuccino":
        if water >= MENU["cappuccino"]["ingredients"]["water"] and coffee >= MENU["cappuccino"]["ingredients"]["coffee"] and milk >= MENU["cappuccino"]["ingredients"]["milk"]:
            print("I can make you a cappuccino")
        else:
            print("I can't make you a cappuccino")
            can_make=False


    #TODO 5>> Process coins

    if can_make:
        print("Insert Coins: ")
        inserted_quarters=int(input("How many quarters?>>> "))
        inserted_nickels=int(input("How many nickels?>>> "))
        inserted_pennies=int(input("How many pennies?>>> "))
        inserted_dimes=int(input("How many dimes?>>> "))

        quarters=inserted_quarters*money_values["quarters"]
        nickels=inserted_nickels*money_values["nickels"]
        pennies=inserted_pennies*money_values["pennies"]
        dimes=inserted_dimes*money_values["dimes"]
        total_inserted_money=quarters+nickels+pennies+dimes
        total_money+=total_inserted_money
        os.system('cls')
        print(logo)

    #TODO 6>> Check if the transaction is successful


    if can_make:
        if total_inserted_money >= MENU["cappuccino"]["cost"]:
            change=total_inserted_money-MENU["cappuccino"]["cost"]
            print(f"Here is your change>>> ${round(change,2)}")
            total_money-=change
        else:
            print(f"Not enough money! Here is your refund>>> ${round(total_inserted_money,2)}")
            total_money-=total_inserted_money
            can_make=False


    #TODO 7>> Make Coffee

    if can_make:
        if first_input=="cappuccino":
            milk-=MENU["cappuccino"]["ingredients"]["milk"]
            water-=MENU["cappuccino"]["ingredients"]["water"]
            coffee-=MENU["cappuccino"]["ingredients"]["coffee"]
            print("Here is your cappuccino ☕")
        elif first_input=="latte":
            milk-=MENU["latte"]["ingredients"]["milk"]
            water-=MENU["latte"]["ingredients"]["water"]
            coffee-=MENU["latte"]["ingredients"]["coffee"]
            print("Here is your latte ☕")
        elif first_input=="espresso":
            milk-=MENU["espresso"]["ingredients"]["milk"]
            water-=MENU["espresso"]["ingredients"]["water"]
            coffee-=MENU["espresso"]["ingredients"]["coffee"]
            print("Here is your espresso ☕")
    