import random

from blackjack.card import Card


class Shuffler():
    def shuffle(self, cards):
        return None


class DefaultShuffler(Shuffler):
    def shuffle(self, cards):
        return random.sample(cards, len(cards))


class NoShuffler(Shuffler):
    def shuffle(self, cards):
        return cards


class Deck:

    def __init__(self, number_of_cards, shuffler=None):
        self.shuffler = shuffler
        if self.shuffler is None:
            self.shuffler = DefaultShuffler()

        cards = []
        for card in number_of_cards:
            for i in range(number_of_cards[card]):
                cards.append(card)

        self.cards = self.shuffler.shuffle(cards)

    def next(self):
        return self.cards.pop(0)

    def number_of_cards(self):
        return len(self.cards)


class NormalDeck(Deck):

    def __init__(self):
        super().__init__({
            Card.TWO: 4,
            Card.THREE: 4,
            Card.FOUR: 4,
            Card.FIVE: 4,
            Card.SIX: 4,
            Card.SEVEN: 4,
            Card.NINE: 4,
            Card.TEN: 4,
            Card.JACK: 4,
            Card.QUEEN: 4,
            Card.KING: 4,
            Card.ACE: 4,
        })
