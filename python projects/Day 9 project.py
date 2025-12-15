
# TODO      For todays project, come up with a way to make an auction like scenario.
# TODO      You will need to make a dictionary to save inputs, make a while statement to run through different users wanting
# TODO      to place a bid, and when there are no more users, have the game announce the winner by name and bid.
#*          Solution starts on line 100.






























































































# bids = {}
# bidding_finished = False

# def find_highest(bidding_record):
#     highest_bid = 0
#     winner = ""

#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"Winner with the highest bid of {highest_bid} is {winner}!")

# while not bidding_finished:
#     name = input("What is your name? ")
#     price = int(input("What is your bid? "))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
#     if should_continue == "no":
#         bidding_finished = True
#         find_highest(bids)
#     elif should_continue == "yes":
#         print("\n" * 100)