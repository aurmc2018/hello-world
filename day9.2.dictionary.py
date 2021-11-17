# import os
from art1 import logo
print(logo)

bidder_dictionary= {}
bidder = True

while bidder:
    # os.system("cls")
    bidder_name  = input("Enter Bidder name")
    bidder_price = input("Enter Bidder price")

    bidder_dictionary[bidder_name] = bidder_price

    continue_bidder = input("Still More bidders yes/no ").lower()

    if continue_bidder == "no":
        bidder = False
        break

print(bidder_dictionary)

def find_highest_bidder(bidder_dictionary):
    highest_bid =0
    winner=""
    for bidder in bidder_dictionary:
        bid_amount = int(bidder_dictionary[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner} for bid of ${highest_bid}")

find_highest_bidder(bidder_dictionary)

