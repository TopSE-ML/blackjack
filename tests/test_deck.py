import unittest

from blackjack.card import Card
from blackjack.deck import Deck, NoShuffler


class TestDeck(unittest.TestCase):

    def test_create_deck(self):
        cards = {
            Card.ACE: 1,
            Card.TWO: 1,
        }
        deck = Deck(cards, NoShuffler())

        self.assertEqual(Card.ACE, deck.next())
        self.assertEqual(Card.TWO, deck.next())

    def test_number_of_cards(self):
        cards = {
            Card.ACE: 1,
            Card.TWO: 1,
        }
        deck = Deck(cards)
        deck.next()

        self.assertEqual(1, deck.number_of_cards())