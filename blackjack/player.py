from abc import ABCMeta, abstractmethod

from blackjack.action import Action


class Player(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def action(self, game):
        raise NotImplementedError()


class DefaultPlayer(Player):

    def action(self, game):
        hand = game.get_player_hand(self)
        return Action.HIT if hand.score() < 17 else Action.STAND