import itertools

from blackjack.deck import NormalDeck
from blackjack.game import Game
from blackjack.player import DefaultPlayer


def do_game(players):
    game = Game()
    game.setup(NormalDeck(), players)
    game.play()
    game.show_result()


def do_games(number_of_games, players):
    combinations = itertools.permutations(players)
    for players in combinations:
        for i in range(number_of_games):
            do_game(players)


do_games(10000, [
    DefaultPlayer('Player1'),
    DefaultPlayer('Player2'),
    DefaultPlayer('Player3'),
    DefaultPlayer('Player4'),
])
