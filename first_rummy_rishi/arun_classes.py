import random

class CardCollection:
    def set_cards(self, cards):
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, index):
        return self.cards.pop(index)

    def show_cards(self):
        card_list = []
        for card in self.cards:
            card_list.append(card)

        return card_list

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_card(self):
        return self.suit + self.rank


def card_value(card):
    r = card.rank
    x = 0
    if r == "J" or r == "Q" or r == "K":
        x = 10
    elif r == "A":
        x = 12
    else:
        x = int(r)
        
    return x
    
class Deck(CardCollection):
    def create_deck(self):
        suits = ["S", "H", "D", "C"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cards = []
        for s in suits:
            for r in ranks:
                c = Card(s, r)
                cards.append(c)
        self.set_cards(cards)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def is_empty(self):
        return len(self.cards) == 0
    

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.laid = []
        self.meld_points = 0

    def draw(self, card):
        self.hand.append(card)

    def discard(self, index):
        return self.hand.pop(index)

    def show_hand(self):
        output = ""
        for i in range(len(self.hand)):
            output += "(" + str(i) + ")" + self.hand[i].get_card() + " "
        return output

    def lay_group(self, indices):
        indices.sort(reverse=True)
        group = []
        for i in indices:
            group.append(self.hand.pop(i))
        group.reverse()
        self.laid.append(group)
        return group
    
    def items(self):
        return self.hand

    def score_hand(self):
        total = 0
        for c in self.hand:
            r = c.rank
            if r in ("J", "Q", "K"):
                total += 10
            elif r == "A":
                total += 1
            else:
                try:
                    total += int(r)
                except ValueError:
                    total += 0
        return total

    def arrange_sets(self):
        rank_order = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        new_hand = []
        for r in rank_order:
            for c in self.hand:
                if c.rank == r:
                    new_hand.append(c)
        self.hand = new_hand

    def arrange_sequences(self):
        rank_order = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        def keyfunc(c):
            # find index of rank in rank_order
            idx = 0
            try:
                idx = rank_order.index(c.rank)
            except Exception:
                idx = 0
            return (c.suit, idx)
        self.hand.sort(key=keyfunc)


class Table(CardCollection):
    def __init__(self, deck):
        # deck: Deck instance used as stock
        self.stock = deck
        self.discard = []  # top is at end of list
        self.cards = []  # table melds 
        self.first_turn = True

    def top_discard(self):
        out = None
        if self.discard:
            out = self.discard[-1]
        return out

    def show_discard(self):
        # return list of card-strings from bottom(0) to top(-1)
        out = []
        for c in self.discard:
            out.append(c.get_card())
        return out

    def take_stock(self):
        out = None
        if self.stock and not self.stock.is_empty():
            out = self.stock.deal_card()
        return out

    def take_discard(self, index_from_bottom):
        out = []
        if self.discard:
            if index_from_bottom >= 0:
                if index_from_bottom < len(self.discard):
                    card = self.discard.pop(index_from_bottom)
                    out.append(card)
            else:
                try:
                    card = self.discard.pop(index_from_bottom)
                    out.append(card)
                except Exception:
                    pass
        return out

    def add_discard(self, card):
        self.discard.append(card)

    def add_meld(self, meld):
        self.cards.append(meld)

    def add_to_meld(self, index, card_entry):
        if index >= 0 and index < len(self.cards):
            self.cards[index][1].append(card_entry)

    

    def show_melds(self):
        out = []
        for m in self.cards:
            meld_display = []
            if isinstance(m, list) and len(m) >= 2:
                entries = m[1]
                i = 0
                while i < len(entries):
                    e = entries[i]
                    card = e[0]
                    owner = e[1]
                    meld_display.append((card.get_card(), owner))
                    i += 1
            out.append(meld_display)
        return out