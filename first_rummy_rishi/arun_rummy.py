# Title: Baseball Game
# Date: October 27, 2025
# Programmers: Arun Rajakumar
# Description: This is a 2-player Rummy game where players take turns drawing and discarding cards,
#           laying down melds, and adding to existing melds until one player empties their hand or the stock runs out.


###############################################################################

from arun_classes import Card, Deck, Player, Table
import arun_classes

def setup_game():
    deck = Deck()
    deck.create_deck()
    deck.shuffle_deck()

    p1 = Player("Player 1")
    p2 = Player("Player 2")
    

    for i in range(13):
        p1.draw(deck.deal_card())
        p2.draw(deck.deal_card())

    table = Table(deck)

    return p1, p2, table, deck

def take_turn(player, table):
    print("\n" + player.name + "'s turn")
    print("Hand:", player.show_hand())
    top = table.top_discard()
    print("Top of discard:", top.get_card() if top else "(none)")
    print("Discard pile:", table.show_discard())
    if table.cards:
        print("Table melds:", table.show_melds())

    # allow arranging without consuming turn
    drawing = True
    while drawing:
        if table.first_turn:
            print("First turn: you cannot pick up from discard; drawing from stock automatically.")
            card = table.take_stock()
            if card:
                player.draw_card(card)
                print("Drew", card.get_card())
            else:
                print("Stock is empty.")
            table.first_turn = False
            drawing = False
            continue
        choice = input("Draw from (S)tock, (D)iscard, or (A)rrange? ").strip().upper()

        if choice == 'A':
            typ = input("Arrange by (S)equences or (R)anks? ").strip().upper()
            if typ == 'S':
                player.arrange_sequences()
            else:
                player.arrange_sets()
            print("Hand:", player.show_hand())
            continue

        if choice == "S":
            card = table.take_stock()
            if card:
                player.draw_card(card)
                print("Drew", card.get_card())
            else:
                print("Stock is empty.")
            table.first_turn = False
            drawing = False
            continue

        if choice == "D":
            if not table.discard:
                print("Discard is empty — cannot take from discard.")
                continue
            index = int(input("Which discard index to take (0 = bottom)? "))
            taken = table.take_discard(index)
            taken_strs = []
            for c in taken:
                taken_strs.append(c.get_card())
            print("Took cards:", taken_strs)
            for c in taken:
                player.draw_card(c)
            table.first_turn = False
            drawing = False
            continue

        print("Invalid choice; try again.")
    # allow adding to existing melds
    if table.cards:
        addm = input("Add to existing meld? (y/n): ").strip().lower()
        if addm == 'y':
            print("Melds:", table.show_melds())
            mi = int(input("Which meld index to add to? "))
            hi = int(input("Which hand index to add? "))
            if hi < 0 or hi >= len(player.hand):
                print("Invalid hand index")
            elif mi < 0 or mi >= len(table.cards):
                print("Invalid meld index")
            else:
                card = player.discard_card(hi)
                table.add_to_meld(mi, [card, player.name])
                player.meld_points += arun_classes.card_value(card)
                print("Added to meld.")

    act = input("Lay down meld? (y/n): ").strip().lower()
    if act == "y":
        idxs = input("Enter hand indices (space separated): ").strip().split()
        ids = []
        for x in idxs:
            if x.isdigit():
                ids.append(int(x))
        
        group = player.lay_group(ids)
        meld_entries = []
        for c in group:
            meld_entries.append([c, player.name])
        table.add_meld(meld_entries)
        for c in group:
            player.meld_points += arun_classes.card_value(c)
        print("Laid down meld.")

    disc = int(input("Choose card to discard by index: "))
    card = player.discard_card(disc)
    table.add_discard(card)
    print("Discarded", card.get_card())

def main():
    print("Welcome to 2-Player Rummy!")
    p1, p2, table, deck = setup_game()

    current = p1
    other = p2

    while not deck.is_empty():
        take_turn(current, table)

        if len(current.items) == 0:
            print(current.name, "wins by emptying hand!")
            break

        current, other = other, current

    print("\n--- Final Scores ---")
    print(p1.name, ":", p1.score_hand(), "points")
    print(p2.name, ":", p2.score_hand(), "points")

    if p1.score_hand() < p2.score_hand():
        print(p1.name, "wins!")
    elif p2.score_hand() < p1.score_hand():
        print(p2.name, "wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
