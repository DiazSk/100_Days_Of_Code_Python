import os

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    max(bidding_record)

    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $ "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')



