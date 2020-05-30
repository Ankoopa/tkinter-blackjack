import random

card_types = ["Hearts", "Clubs", "Diamonds", "Spades"]
card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
card_faces = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def game():
    dealer_cards = []
    player_cards = []

    player_score = 0
    dealer_score = 0

    while True:
        card = gen_card()
        cardno = card[1]
        dealer_card = card[0]
        if dealer_card not in dealer_cards and dealer_card not in player_cards:
            dealer_cards.append(dealer_card)

            if "Ace" in dealer_card:
                if dealer_score < 11:
                    dealer_score += 11
                else:
                    dealer_score += 1
            else:
                dealer_score += card_values[cardno]

            if len(dealer_cards) == 2:
                break
        else:
            continue

    print("Dealer deals two cards:", dealer_cards)
    print("Dealer score: ", dealer_score)

    if dealer_score == 21:
        print("Blackjack! Dealer Wins!")
        quit()
    elif dealer_score <= 16:
        while dealer_score <= 16:
            dealer_score = stand(dealer_score, player_cards, dealer_cards)
        print("Dealer deals another card:", dealer_cards)
        if dealer_score > 21:
            if any("Ace" in s for s in dealer_cards):
                dealer_score -= 10
            else:
                print("Dealer bust! Player wins!")
                quit()
        elif dealer_score == 21:
            print("Dealer reached 21! Dealer wins!")
            quit()
        print("Dealer score:", dealer_score)

    while True:
        card = gen_card()
        cardno = card[1]
        player_card = card[0]

        if player_card not in dealer_cards and player_card not in player_cards:
            player_cards.append(player_card)

            if "Ace" in player_card:
                if player_score < 11:
                    player_score += 11
                else:
                    player_score += 1
            else:
                player_score += card_values[cardno]

            if len(player_cards) == 2:
                break
        else:
            continue

    print("Player deals two cards:", player_cards)
    print("Player score: ", player_score)

    if player_score == 21:
        print("Blackjack! Player wins!")
        quit()

    while dealer_score < 21 and player_score < 21:
        choice = str.lower(input("Hit or stand: "))

        if choice == "hit":
            player_score = player_hit(player_score, player_cards, dealer_cards)
            print(player_cards)
            print(player_score)
        elif choice == "stand":
            break

    if player_score > 21:
        print("Player bust! Dealer wins!")
    elif player_score < 21:
        if player_score > dealer_score and dealer_score < 21:
            while dealer_score < 21:
                dealer_score = stand(dealer_score, player_cards, dealer_cards)
                if dealer_score > 21:
                    print("Dealer cards:", dealer_cards)
                    print("Dealer score:", dealer_score)
                    print("Dealer bust! Player wins!")
                    quit()

                if dealer_score > player_score:
                    print("Dealer score:", dealer_score)
                    print("Dealer has higher hand. Dealer wins!")
                    quit()
                elif dealer_score == player_score:
                    print("Dealer score:", dealer_score)
                    print("Tie!")
                    quit()
    elif player_score == 21:
        while dealer_score < 21:
            dealer_score = stand(dealer_score, player_cards, dealer_cards)
            if dealer_score == 21:
                print("Dealer Score:", dealer_score)
                print("Tie!")
                quit()
            else:
                print("Dealer Score:", dealer_score)
                print("Dealer bust! Player wins!")
                quit()


def stand(score, p_cards, d_cards):
    while True:
        card = gen_card()
        cardno = card[1]
        dealer_card = card[0]

        if dealer_card not in p_cards and dealer_card not in d_cards:
            d_cards.append(dealer_card)
            if "Ace" in dealer_card:
                if score < 11:
                    score += 11
                else:
                    score += 1
            else:
                score += card_values[cardno]
            return score
        else:
            continue


def player_hit(score, p_cards, d_cards):
    while True:
        card = gen_card()
        cardno = card[1]
        player_card = card[0]

        if player_card not in p_cards and player_card not in d_cards:
            p_cards.append(player_card)
            if "Ace" in player_card:
                if score < 11:
                    score += 11
                else:
                    score += 1
            else:
                score += card_values[cardno]
            return score
        else:
            continue


def gen_card():
    cardtype = card_types[random.randint(0, len(card_types) - 1)]
    cardno = random.randint(0, len(card_values) - 1)
    card = card_faces[cardno] + " of " + cardtype
    return card, cardno


game()
