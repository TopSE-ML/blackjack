import unittest

from blackjack.card import Card
from blackjack.hand import Hand


class TestHand(unittest.TestCase):

    @staticmethod
    def make_hand(cards):
        hand = Hand()
        for card in cards:
            hand.add(card)

        return hand

    def test_score_is_0_when_created(self):
        hand = Hand()
        self.assertEqual(0, hand.score())

    def test_score_is_2_when_hand_contains_only_two(self):
        hand = self.make_hand([Card.TWO])
        self.assertEqual(2, hand.score())

    def test_score_is_10_when_hand_contains_only_king(self):
        hand = self.make_hand([Card.KING])
        self.assertEqual(10, hand.score())

    def test_score_is_11_when_hand_contains_only_ace(self):
        hand = self.make_hand([Card.ACE])
        self.assertEqual(11, hand.score())

    def test_score_is_13_when_hand_contains_eight_and_five(self):
        hand = self.make_hand([Card.EIGHT, Card.FIVE])
        self.assertEqual(13, hand.score())

    def test_score_is_17_when_hand_contains_seven_and_king(self):
        hand = self.make_hand([Card.SEVEN, Card.KING])
        self.assertEqual(17, hand.score())

    def test_score_is_20_when_hand_contains_nine_and_queen_and_ace(self):
        hand = self.make_hand([Card.NINE, Card.QUEEN, Card.ACE])
        self.assertEqual(20, hand.score())

    def test_score_is_22_when_hand_contains_jack_queen_and_two(self):
        hand = self.make_hand([Card.JACK, Card.QUEEN, Card.TWO])
        self.assertEqual(22, hand.score())

    def test_score_is_12_when_hand_contains_two_aces(self):
        hand = self.make_hand([Card.ACE, Card.ACE])
        self.assertEqual(12, hand.score())

    def test_get_0_returns_first_card(self):
        hand = self.make_hand([Card.ACE])
        self.assertEqual(Card.ACE, hand.get(0))

    def test_lose_if_player_bust(self):
        player = self.make_hand([Card.TEN, Card.JACK, Card.TWO])
        dealer = self.make_hand([Card.TWO, Card.TWO])
        result = Hand.check(player, dealer)

        self.assertEqual("LOSE", result)

    def test_lose_if_player_smaller_than_dealer(self):
        player = self.make_hand([Card.TEN, Card.SIX])
        dealer = self.make_hand([Card.JACK, Card.EIGHT])
        result = Hand.check(player, dealer)

        self.assertEqual("LOSE", result)

    def test_win_if_player_smaller_than_dealer(self):
        player = self.make_hand([Card.TEN, Card.NINE])
        dealer = self.make_hand([Card.JACK, Card.EIGHT])
        result = Hand.check(player, dealer)

        self.assertEqual("WIN", result)

    def test_win_if_only_dealer_is_bust(self):
        player = self.make_hand([Card.TEN, Card.NINE])
        dealer = self.make_hand([Card.JACK, Card.EIGHT, Card.FIVE])
        result = Hand.check(player, dealer)

        self.assertEqual("WIN", result)

    def test_draw(self):
        player = self.make_hand([Card.TEN, Card.NINE])
        dealer = self.make_hand([Card.JACK, Card.EIGHT, Card.ACE])
        result = Hand.check(player, dealer)

        self.assertEqual("DRAW", result)

    def test_blackjack_win_21(self):
        player = self.make_hand([Card.TEN, Card.ACE])
        dealer = self.make_hand([Card.JACK, Card.EIGHT, Card.THREE])
        result = Hand.check(player, dealer)

        self.assertEqual("WIN", result)