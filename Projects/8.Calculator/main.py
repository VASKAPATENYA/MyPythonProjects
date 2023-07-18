from art import logo
import os
print(logo)


#Add
def add(n1, n2):
    return n1+n2

#Substract
def sub(n1, n2):
    return n1-n2

#Multiply
def multiply(n1, n2):
    return n1*n2

#Divide
def divide(n1, n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide
}

def calculate():
    num1=float(input("Enter a number>> "))
    should_continue=True
    while should_continue:

        for i in operations:
            print(i)
        operation_symbol=input("Pick an operation from the line above>> ")

        num2=float(input("Enter a number>> "))

        operation=operations[operation_symbol]
        answer=operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue=input("Type 'y' to continue calcuating with this number or type 'n' to start over or type 'e' to exit>> ")

        if should_continue=="y":
            num1=answer
        elif should_continue=="n":
            should_continue=False
            os.system('cls')
            print(logo)
            calculate()
        elif should_continue=="e":
            os.system('cls')
            print(logo)
            print("Thanks for using this!")
            break


calculate()