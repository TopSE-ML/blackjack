import unittest
from unittest import mock

from blackjack.action import Action
from blackjack.card import Card
from blackjack.deck import NormalDeck, Deck, NoShuffler
from blackjack.game import Game, GameIsNotInitializedException, GameIsNotFinishedException
from blackjack.player import Player


class StandPlayer(Player):

    def action(self, game):
        return Action.STAND


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_game_is_not_initialized_when_an_instance_was_created(self):
        self.assertFalse(self.game.is_initialized())

    def test_game_is_initialized_after_setup_function_was_called(self):
        self.game.setup(NormalDeck(), [
            StandPlayer('Player 1'),
            StandPlayer('Player 2'),
            StandPlayer('Player 3'),
            StandPlayer('Player 4'),
        ])

        self.assertTrue(self.game.is_initialized())

    def test_game_provide_initial_hands(self):
        p = StandPlayer('Player 1'),
        self.game.setup(Deck({Card.ACE: 1, Card.TWO: 1, Card.THREE: 1, Card.FOUR: 1}, NoShuffler()), [ p ])

        hand = self.game.get_player_hand(p)
        self. assertEqual(Card.ACE, hand.get(0))
        self. assertEqual(Card.TWO, hand.get(1))

    def test_game_provide_dealer_up_card(self):
        p = StandPlayer('Player 1'),
        self.game.setup(Deck({Card.ACE: 1, Card.TWO: 1, Card.THREE: 1, Card.FOUR: 1}, NoShuffler()), [ p ])

        up_card = self.game.get_dealer_up_card()
        self.assertEqual(Card.THREE, up_card)

    def test_game_does_not_provide_hands_if_game_is_not_setup(self):
        with self.assertRaises(GameIsNotInitializedException):
            self.game.get_player_hand(0)

    def test_game_does_not_provide_dealer_up_card_if_game_is_not_setup(self):
        with self.assertRaises(GameIsNotInitializedException):
            self.game.get_dealer_up_card()

    def test_game_does_not_provide_dealer_hand_if_game_is_not_finished(self):
        p = StandPlayer('Player 1')
        self.game.setup(Deck({Card.ACE: 1, Card.TWO: 1, Card.THREE: 1, Card.FOUR: 1}, NoShuffler()), [ p ])

        with self.assertRaises(GameIsNotFinishedException):
            self.game.get_dealer_hand()

    def test_game_provide_dealer_hand_if_game_was_finished(self):
        p = StandPlayer('Player 1')
        self.game.setup(Deck({Card.ACE: 1, Card.TWO: 1, Card.JACK: 1, Card.KING: 1}, NoShuffler()), [ p ])
        self.game.play()

        hand = self.game.get_dealer_hand()
        self.assertEqual(20, hand.score())

    def test_game_call_player_action(self):
        p = StandPlayer('Player 1')

        self.game.setup(Deck({Card.ACE: 1, Card.TWO: 1, Card.TEN: 1, Card.JACK: 1}, NoShuffler()), [ p ])
        self.game.play()

        hand = self.game.get_player_hand(p)
        self.assertEqual(13, hand.score())

    def test_game_call_player_action(self):
        p = StandPlayer('Player 1')
        p.action = mock.MagicMock(side_effect=[Action.HIT, Action.STAND])

        self.game.setup(Deck({Card.ACE: 1, Card.TWO: 1, Card.JACK: 1, Card.QUEEN: 1, Card.EIGHT: 1 }, NoShuffler()), [ p ])
        self.game.play()

        hand = self.game.get_player_hand(p)
        self.assertEqual(21, hand.score())

        hand = self.game.get_dealer_hand()
        self.assertEqual(20, hand.score())

    def test_dealer_have_to_hit_if_score_is_lower_than_17(self):
        p = StandPlayer('Player 1')
        self.game.setup(Deck({Card.ACE: 1, Card.TWO: 1, Card.SIX: 1, Card.QUEEN: 1, Card.EIGHT: 1 }, NoShuffler()), [ p ])
        self.game.play()

        hand = self.game.get_player_hand(p)
        self.assertEqual(13, hand.score())

        hand = self.game.get_dealer_hand()
        self.assertEqual(24, hand.score())
