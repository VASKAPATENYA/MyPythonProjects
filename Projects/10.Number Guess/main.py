from art import logo
import random
import os
print(logo)

# lives=""
# number=random.randint(1,101)
should_continue=True

def setup():
    lives=""
    number=random.randint(1,101)
    print(number)
    print("THE NUMBER IS BETWEEN 1 AND 100")
    difficulty=input("CHOOSE A DIFFICULTY. TYPE 'easy' FOR EASY OR TYPE 'hard' FOR HARD>>> ")
    if difficulty=="easy":
        lives=10
    elif difficulty=="hard":
        lives=5

    print(f"You have {lives} lives left!")
    return (lives,number)

lives,number=setup()

while should_continue:
    guess=int(input("Make a guess>>> "))
    if guess == number:
        print("Well Done!")
        should_continue=False
    elif guess > number:
        print("Too High!") 
        print("Try Again!")
        lives-=1
        print(f"You have {lives} lives left!")
    elif guess < number:
        print("Too Low!") 
        print("Try Again!")
        lives-=1
        print(f"You have {lives} lives left!")
    if lives==1:
        print("You Lost!")
        print(f"The Number Was>>> {number}")
        should_continue=False
    if should_continue==False:
        answer=input("Would You Like to Play Again? Yes/No>>> ")
        if answer=="yes":
            os.system('cls')
            print(logo)
            lives,number=setup()
            should_continue=True
        if answer=="no":
            os.system('cls')
            print(logo)
            print("Thanks For Playing!")
            should_continue=False
                