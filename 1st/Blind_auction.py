from replit import clear

# Hint; you can clear() to clear output in the console


higher_bid = 0
bidding_finished = False
bids = {}


def find_higher_bidder(bidding_record):
    global winner, higher_bid
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > higher_bid:
            higher_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of {higher_bid}')


while not bidding_finished == True:
    name = input("What is your name?:\n")
    price = int(input("What is your bid\n"))
    bids[name] = price
    should_continue = input("Are there any other bidder? Type Yes or No\n")
    if should_continue == "yes":
        bidding_finish = False
        clear()
    # find_the_highest_bidder(bids)
    else:
        bidding_finish = True
        find_higher_bidder(bids)
        print(bids)

#################################################################

# from replit import clear
# bids = {}
# bidding_finished = False
#
#
# def greater_value(bids_record):
#     greater = max(bids_record)
#     print( greater)
#
#
# while not bidding_finished:
#     name = input('Enter the name of the bidder: ')
#     price = int(input('Enter the Price of the bidder: '))
#     bids[name] = price
#     should_continue = input('If is ther any other bidder: type y or n: ')
#     if should_continue == 'y':
#         bidding_finished = False
#         clear()
#     else:
#         bidding_finished = True
#         greater_value(bids)
