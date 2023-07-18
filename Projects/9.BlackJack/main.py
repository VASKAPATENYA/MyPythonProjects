from art import logo
import time
import random
import os
print(logo)


deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Fonctions
def player_hit():
    total=sum(players_cards)
    if total>10:
        deck[0]=1
    players_cards.append(random.choice(deck))
    time.sleep(1)
    print(f"The Players Cards Are>>> {players_cards}, {sum(players_cards)}")

def dealer_hit():
    total=sum(dealers_cards)
    if total>10:
        deck[0]=1
    dealers_cards.append(random.choice(deck))
    time.sleep(1)
    print(f"The Dealers Cards Are>>> {dealers_cards}, {sum(dealers_cards)}")

def control():
    if sum(players_cards)>sum(dealers_cards):
        time.sleep(1)
        print("Well Done You Won!")
    elif sum(players_cards)<sum(dealers_cards):
        time.sleep(1)
        print("Ooops You Lost!")
    if sum(players_cards)==sum(dealers_cards):
        time.sleep(1)
        print("Draw!")    

should_restart=True
while should_restart:
    players_cards=[]
    dealers_cards=[]
    should_hit=True
    player_hit()
    player_hit()
    dealer_hit()

    while should_hit and sum(players_cards)<21:
        answer=input("Type 'h' to hit or type 's' to stand>>> ")

        if answer=="h":
            player_hit()
            if sum(players_cards)>21:
                time.sleep(1)
                print(f"You loose with {sum(players_cards)}")

        if answer=="s":
            dealer_hit()
            dealer_hit()
            while sum(dealers_cards)<17:
                dealer_hit()
                time.sleep(1)
                print(f"The Players Cards Are>>> {players_cards}, {sum(players_cards)}")
            time.sleep(1)
            print(f"The Players Cards Are>>> {players_cards}, {sum(players_cards)}")
            time.sleep(1)
            print(f"The Dealers Cards Are>>> {dealers_cards}, {sum(dealers_cards)}")
            if sum(dealers_cards)>21:
                time.sleep(1)
                print("You Win!")
            should_hit=False
    if sum(dealers_cards)<=21 and sum(players_cards)<=21:
        control()
    start_over=input("Type 'y' if you wanna restart the game or type 'q' quit>>> ")

    if start_over=="y":
        os.system('cls')
        print(logo)
    elif start_over=="q":
        os.system('cls')
        print(logo)
        print("Thanks for playing!")
        should_restart=False