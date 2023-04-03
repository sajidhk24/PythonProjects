import random
# from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """ Return random cards from cards """

    card = random.choice(cards)
    return card


def calcualate_cards(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)


def compare(users_score, computers_score):
    if computers_score == users_score:
        return 'Draw'
    elif computers_score == 0:
        return 'Lose, Opponent has Black Jack'
    elif users_score == 0:
        return 'Win with a Black Jack'
    elif computers_score > 21:
        return "Opponent went over and you Win"
    elif users_score > 21:
        return "You went over and Lose"
    else:
        return 'You Lose'


def play_game():
    global computers_score, user_score
    users_card = []
    computers_cards = []
    for _ in range(2):
        # new_card = [deal_card()]
        users_card.append(deal_card())
        computers_cards.append(deal_card())
        # print(users_card,computers_cards)
    is_game_over = False
    while not is_game_over:

        user_score = calcualate_cards(users_card)
        computers_score = calcualate_cards(computers_cards)
        print(f'{user_score} and {users_card}')
        print(f'computers first card is {computers_cards[0]}')
        if user_score == 0 or computers_score == 0 or user_score > 21:
            is_game_over = True
        else:
            users_deal = input('Type "y" if you want to draw another card else "n":\n')
            if users_deal == "y":
                users_card.append(deal_card())
            else:

                is_game_over = True

    while computers_score != 0 and computers_score < 17:
        computers_cards.append(deal_card())
        computers_score = calcualate_cards(computers_cards)
        print(f'Computers cards is {computers_cards}')
    print(f'Your final hand is {users_card} and your final score is {user_score}')
    print(f'Computers final hand is {computers_cards} and computers final score is {computers_score}')
    print(compare(user_score, computers_score))


while input("Do you want to Play Black Jack? Type 'y' for Yes and 'n' for No:\n") == 'y':
    # clear()
    play_game()