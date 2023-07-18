from art import logo
import os
print(logo)

bids={}
bidding_finished=False

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The highest bidder is {winner} with ${highest_bid}")


while not bidding_finished:
    name=input("Name>> ")
    bid=int(input("Bid>> "))
    bids[name]=bid
    should_continue=input("Are there any other biders? Y/N>> ")
    if  should_continue=="n":
        bidding_finished=True
        find_highest_bidder(bids)
    elif should_continue=="y":
        os.system('cls')
