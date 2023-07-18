from art import logo,vs
from data import data
import random
import os
print(logo)
should_continue=True
score=0
account_b=random.choice(data)

def format_data(account):
    account_name=account["name"]
    account_desc=account["description"]
    account_country=account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(answer, a_followers, b_followers):
    if a_followers>b_followers:
        return answer == "a"
    else:
        return answer=="b"

while should_continue:
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    answer=input("Who has more followers? Type 'A' or 'B'>>> ").lower()

    a_follow_count=account_a["follower_count"]
    b_follow_count=account_b["follower_count"]

    is_correct=check_answer(answer, a_follow_count, b_follow_count)
    if is_correct:
        score+=1
        os.system('cls')
        print(logo)
        print(f"That's Right. Score:{score}")
    else:
        print(f"Oops! Final Score: {score}")
        should_again=input("Would you Like To Play Again? Y/N >>>").lower()
        if should_again=="n":
            should_continue=False
            os.system('cls')
            print(logo)
            print("Thanks For Playing!")
        else:
            os.system('cls')
            print(logo)

