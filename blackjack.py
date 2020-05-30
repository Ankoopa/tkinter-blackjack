from tkinter import *
from tkinter import messagebox
import random

root = Tk()
tk_var = StringVar()
root.title("Blackjack Game")

card_types = ["Hearts", "Clubs", "Diamonds", "Spades"]
card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
card_faces = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

def game():
    dealer_cards = []
    player_cards = []

    player_score = 0
    dealer_score = 0

    player_turns = 0
    dealer_turns = 0

    p_cards_imgs = [p_card1, p_card2, p_card3, p_card4, p_card5, p_card6, p_card7, p_card8, p_card9]
    d_cards_imgs = [d_card1, d_card2, d_card3, d_card4, d_card5, d_card6, d_card7, d_card8, d_card9]

    while len(dealer_cards) < 2:
        card = gen_card()
        cardno = card[1]
        dealer_card = card[0]
        if dealer_card not in dealer_cards and dealer_card not in player_cards:
            d_card_img = PhotoImage(file=dealer_card + ".gif")
            dealer_cards.append(dealer_card)
            d_cards_imgs[dealer_turns].config(image=d_card_img)
            d_cards_imgs[dealer_turns].image = d_card_img

            if "Ace" in dealer_card:
                if dealer_score < 11:
                    dealer_score += 11
                else:
                    dealer_score += 1
            else:
                dealer_score += card_values[cardno]

            dealer_turns += 1
        else:
            continue

    status_lbl.config(text="Dealer deals two cards...")
    dlr_score.config(text="Dealer score: " + str(dealer_score))

    if dealer_score == 21:
        status_lbl.config(text="Blackjack! Dealer Wins!")

        replay = messagebox.askyesno("Replay", "Do you want to play again?")
        if replay:
            reset_cards(p_cards_imgs, d_cards_imgs)
            game()
        else:
            quit()
        root.mainloop()
    elif dealer_score <= 16:
        status_lbl.config(text="Dealer deals another card.")
        while dealer_score <= 16:
            dealer_score = stand(dealer_score, player_cards, dealer_cards)
            d_card_img = PhotoImage(file=dealer_cards[-1] + ".gif")
            d_cards_imgs[dealer_turns].config(image=d_card_img)
            d_cards_imgs[dealer_turns].image = d_card_img
            dealer_turns += 1
        if dealer_score > 21:
            if any("Ace" in s for s in dealer_cards):
                dealer_score -= 10
                dlr_score.config(text="Dealer score: " + str(dealer_score))
            else:
                dlr_score.config(text="Dealer score: " + str(dealer_score))
                status_lbl.config(text="Dealer bust! Player wins!")
                print("Dealer bust! Player wins!")
                replay = messagebox.askyesno("Replay", "Do you want to play again?")
                if replay:
                    reset_cards(p_cards_imgs, d_cards_imgs)
                    game()
                else:
                    quit()
                root.mainloop()
        elif dealer_score == 21:
            dlr_score.config(text="Dealer score: " + str(dealer_score))
            status_lbl.config(text="Dealer reached 21. Dealer wins!")
            print("Dealer reached 21! Dealer wins!")
            replay = messagebox.askyesno("Replay", "Do you want to play again?")
            if replay:
                reset_cards(p_cards_imgs, d_cards_imgs)
                game()
            else:
                quit()
            root.mainloop()
        dlr_score.config(text="Dealer score: " + str(dealer_score))

    while len(player_cards) < 2:
        card = gen_card()
        cardno = card[1]
        player_card = card[0]

        if player_card not in dealer_cards and player_card not in player_cards:
            p_card_img = PhotoImage(file=player_card + ".gif")
            p_cards_imgs[player_turns].config(image=p_card_img)
            p_cards_imgs[player_turns].image = p_card_img
            player_cards.append(player_card)

            if "Ace" in player_card:
                if player_score < 11:
                    player_score += 11
                else:
                    player_score += 1
            else:
                player_score += card_values[cardno]

            player_turns += 1
        else:
            continue

    status_lbl.config(text="Player deals two cards...")
    plr_score.config(text="Player score: "+str(player_score))

    if player_score == 21:
        status_lbl.config(text="Blackjack! Player wins!")
        replay = messagebox.askyesno("Replay", "Do you want to play again?")
        if replay:
            reset_cards(p_cards_imgs, d_cards_imgs)
            game()
        else:
            quit()
        root.mainloop()

    while dealer_score < 21 and player_score < 21:
        status_lbl.config(text="Status: Hit or Stand?")
        root.wait_variable(tk_var)
        choice = tk_var.get()

        if choice == "hit":
            player_score = player_hit(player_score, player_cards, dealer_cards)
            p_card_img = PhotoImage(file=player_cards[-1] + ".gif")
            p_cards_imgs[player_turns].config(image=p_card_img)
            p_cards_imgs[player_turns].image = p_card_img
            player_turns += 1
            print(player_cards)
            plr_score.config(text="Player score: " + str(player_score))
        elif choice == "stand":
            break

    if player_score > 21:
        status_lbl.config(text="Player bust! Dealer wins!")
        print("Player bust! Dealer wins!")
        replay = messagebox.askyesno("Replay", "Do you want to play again?")
        if replay:
            reset_cards(p_cards_imgs, d_cards_imgs)
            game()
        else:
            quit()
        root.mainloop()
    elif player_score < 21:
        if (player_score > dealer_score or player_score == dealer_score) and dealer_score < 21:
            while dealer_score < 21:
                dealer_score = stand(dealer_score, player_cards, dealer_cards)
                d_card_img = PhotoImage(file=dealer_cards[-1] + ".gif")
                d_cards_imgs[dealer_turns].config(image=d_card_img)
                d_cards_imgs[dealer_turns].image = d_card_img
                dealer_turns += 1
                if dealer_score > 21:
                    print("Dealer cards:", dealer_cards)
                    dlr_score.config(text="Dealer score:" + str(dealer_score))
                    print("Dealer bust! Player wins!")
                    status_lbl.config(text="Dealer bust! Player wins!")
                    replay = messagebox.askyesno("Replay", "Do you want to play again?")
                    if replay:
                        reset_cards(p_cards_imgs, d_cards_imgs)
                        game()
                    else:
                        quit()
                    root.mainloop()

                if dealer_score > player_score:
                    dlr_score.config(text="Dealer score:" + str(dealer_score))
                    status_lbl.config(text="Dealer has higher hand. Dealer wins!")
                    print("Dealer has higher hand. Dealer wins!")
                    replay = messagebox.askyesno("Replay", "Do you want to play again?")
                    if replay:
                        reset_cards(p_cards_imgs, d_cards_imgs)
                        game()
                    else:
                        quit()
                    root.mainloop()
                elif dealer_score == player_score:
                    dlr_score.config(text="Dealer score:" + str(dealer_score))
                    status_lbl.config(text="Dealer and Player tied!")
                    print("Tie!")
                    replay = messagebox.askyesno("Replay", "Do you want to play again?")
                    if replay:
                        reset_cards(p_cards_imgs, d_cards_imgs)
                        game()
                    else:
                        quit()
                    root.mainloop()
        elif player_score < dealer_score:
            status_lbl.config(text="Dealer has higher hand. Dealer wins!")
            print("Dealer has higher hand. Dealer wins!")
            replay = messagebox.askyesno("Replay", "Do you want to play again?")
            if replay:
                reset_cards(p_cards_imgs, d_cards_imgs)
                game()
            else:
                quit()
            root.mainloop()
    elif player_score == 21:
        while dealer_score < 21:
            dealer_score = stand(dealer_score, player_cards, dealer_cards)
            d_card_img = PhotoImage(file=dealer_cards[-1] + ".gif")
            d_cards_imgs[dealer_turns].config(image=d_card_img)
            d_cards_imgs[dealer_turns].image = d_card_img
            dealer_turns += 1
            if dealer_score == 21:
                dlr_score.config(text="Dealer score:" + str(dealer_score))
                status_lbl.config(text="Dealer and Player tied!")
                print("Tie!")
                replay = messagebox.askyesno("Replay", "Do you want to play again?")
                if replay:
                    reset_cards(p_cards_imgs, d_cards_imgs)
                    game()
                else:
                    quit()
                root.mainloop()
            else:
                dlr_score.config(text="Dealer score:" + str(dealer_score))
                print("Dealer bust! Player wins!")
                status_lbl.config(text="Dealer bust! Player wins!")
                replay = messagebox.askyesno("Replay", "Do you want to play again?")
                if replay:
                    reset_cards(p_cards_imgs, d_cards_imgs)
                    game()
                else:
                    quit()
                root.mainloop()


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
            if "Ace" in player_card and score < 21:
                if score < 11:
                    score += 11
                else:
                    score += 1
            elif "Ace" in player_card and score > 21:
                score -= 10
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

def reset_cards(p_cards, d_cards):
    card_img = PhotoImage(file="empty.gif")
    for i in p_cards:
        i.config(image=card_img)
        i.image = card_img
    for i in d_cards:
        i.config(image=card_img)
        i.image = card_img



l_Frame = Frame(root, width=285, height=325, bd=1, relief=SUNKEN)
l_Frame.grid(row=2, column=0, padx=5, pady=5)
r_Frame = Frame(root, width=285, height=325, bd=1, relief=SUNKEN)
r_Frame.grid(row=2, column=1, padx=5, pady=5)
btn_Frame = Frame(root, width=1085, height=15, bd=1)
btn_Frame.grid(row=3, column=1, padx=1, pady=1)
low_Frame = Frame(root, width=1085, height=15, bd=1)
low_Frame.grid(row=4, columnspan=2, padx=10, pady=10)

dealer_lbl = Label(root, text="Dealer", anchor=N, font=("Arial",18))
dealer_lbl.grid(row=0, column=0, pady=10, padx=10)
plr_lbl = Label(root, text="Player", anchor=N, font=("Arial",18))
plr_lbl.grid(row=0, column=1, padx=10, pady=10)
status_lbl = Label(low_Frame, text="Status: Loading...", font=("Arial",22))
status_lbl.grid(row=0, column=0)

dlr_score = Label(root, text="Score: 0", anchor=N, font=("Arial",18))
dlr_score.grid(row=1, column=0, padx=5, pady=5)
plr_score = Label(root, text="Score: 0", anchor=N, font=("Arial",18))
plr_score.grid(row=1, column=1, padx=5, pady=5)

img = PhotoImage(file="empty.gif")
p_card1 = Label(r_Frame, image=img)
p_card1.grid(row=0, column=0)
p_card2 = Label(r_Frame, image=img)
p_card2.grid(row=0, column=1)
p_card3 = Label(r_Frame, image=img)
p_card3.grid(row=0, column=2)
p_card4 = Label(r_Frame, image=img)
p_card4.grid(row=1, column=0)
p_card5 = Label(r_Frame, image=img)
p_card5.grid(row=1, column=1)
p_card6 = Label(r_Frame, image=img)
p_card6.grid(row=1, column=2)
p_card7 = Label(r_Frame, image=img)
p_card7.grid(row=2, column=0)
p_card8 = Label(r_Frame, image=img)
p_card8.grid(row=2, column=1)
p_card9 = Label(r_Frame, image=img)
p_card9.grid(row=2, column=2)

d_card1 = Label(l_Frame, image=img)
d_card1.grid(row=0, column=0)
d_card2 = Label(l_Frame, image=img)
d_card2.grid(row=0, column=1)
d_card3 = Label(l_Frame, image=img)
d_card3.grid(row=0, column=2)
d_card4 = Label(l_Frame, image=img)
d_card4.grid(row=1, column=0)
d_card5 = Label(l_Frame, image=img)
d_card5.grid(row=1, column=1)
d_card6 = Label(l_Frame, image=img)
d_card6.grid(row=1, column=2)
d_card7 = Label(l_Frame, image=img)
d_card7.grid(row=2, column=0)
d_card8 = Label(l_Frame, image=img)
d_card8.grid(row=2, column=1)
d_card9 = Label(l_Frame, image=img)
d_card9.grid(row=2, column=2)

btn_hit = Button(btn_Frame, text="Hit", width=8, height=1, command=lambda: tk_var.set("hit"))
btn_hit.grid(row=0, column=0, padx=2, pady=2, sticky=E)
btn_stand = Button(btn_Frame, text="Stand", width=8, height=1, command=lambda: tk_var.set("stand"))
btn_stand.grid(row=0, column=1, padx=2, pady=2, sticky=E)

game()
