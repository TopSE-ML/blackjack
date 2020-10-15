import unittest

from blackjack.card import Card


class TestGame(unittest.TestCase):

    def test_score_of_two_is_2(self):
        self.assertEqual(2, Card.TWO.score())

    def test_score_of_jack_is_10(self):
        self.assertEqual(10, Card.JACK.score())

    def test_score_of_ace_is_1_or_11(self):
        self.assertEqual([1, 11], Card.ACE.score())
