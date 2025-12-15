
#! Blackjack 
# Todo Deck is unlimited in size, no Jokers, Jack/Queen/King = 10, Ace counts as 11 or 1
# Todo the line below is your list for cards to use.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#* Solution starts on line 100
#@ This is challenging, I wish you the best of luck!




























































































import random

def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def total(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
       
    return sum(cards)

def compare(user_score, dealer_total):
    if user_score == dealer_total:
        return "Its a draw!"
    elif dealer_total == 0:
        return "You Lose, Dealer has blackjack!!!"
    elif user_score == 0:
        return "Winner!!"
    elif user_score > 21:
        return "Bust, You Lose!!!!"
    elif dealer_total > 21:
        return "Dealer Busted, You Win!!!"
    elif user_score > dealer_total:
        return "You Win!!!!!!"
    else:
        return "You Lose!!!!!!"

def play_game(): 
    player_cards = []
    dealer_cards = []
    dealer_score = -1
    player_score = -1
    game_over = False

    for _ in range(2):
        player_cards.append(deal())
        dealer_cards.append(deal())

    while not game_over:
        player_score = total(player_cards)
        dealer_score = total(dealer_cards)
        print(f"The Player has {player_cards}, the total is {player_score}")
        print(f"Dealer has {dealer_cards[0]} ")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over=True
        else:
            keep_going = input("Type 'hit' to get another card, or type 'stand' to stay at what you got? ").lower()
            if keep_going == "hit":
                player_cards.append(deal())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal())
        dealer_score = total(dealer_cards)


    print(f"Player's final hand is: {player_cards}, with a total of {player_score}")
    print(f"Dealer's final hand is: {dealer_cards}, with a total of {dealer_score}")
    print(compare(player_score, dealer_score))


while input("Do you want to play a round of Blackjack? Type 'yes' or 'no': ").lower() == "yes":
    print("\n" * 20)
    play_game()

