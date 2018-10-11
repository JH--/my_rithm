from random import shuffle

# Create a deck of cards class. Internally, the deck of cards should use
#  another class, a card class. Your requirements are:
#
# The Deck class should have a deal method to deal a single card from
# the deck
# After a card is dealt, it is removed from the deck.
# There should be a shuffle method which makes sure the deck of cards
# has all 52 cards and then rearranges them randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and
# a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
#


class Card:
    def __init__(self, rank, suit):
        self.rank, self.suit = rank, suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.make_new_deck()

    def make_new_deck(self):
        ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
        suits = 'Hearts Diamonds Clubs Spades'.split()
        self.deck = [Card(r, s) for r in ranks for s in suits]

    def shuffle(self):
        if len(self.deck) != 52:
            self.make_new_deck()
        shuffle(self.deck)

    def deal(self):
        if len(self.deck) == 0:
            raise ValueError("All the cards have been dealt")
        return self.deck.pop()
