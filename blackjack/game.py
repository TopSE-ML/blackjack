from blackjack.action import Action
from blackjack.hand import Hand


class GameIsNotInitializedException(Exception):
    pass


class GameIsNotFinishedException(Exception):
    pass


class Game:

    def __init__(self):
        self.__initialized = False
        self.__finished = False
        self.__deck = None
        self.__players = []
        self.__hands = dict()
        self.__dealer_hand = Hand()

    def is_initialized(self):
        return self.__initialized

    def setup(self, deck, players):
        self.__initialized = True
        self.__deck = deck
        for player in players:
            self.__players.append(player)
            hand = Hand()
            hand.add(self.__deck.next())
            hand.add(self.__deck.next())
            self.__hands[player] = hand
        self.__dealer_hand.add(self.__deck.next())
        self.__dealer_hand.add(self.__deck.next())

    def play(self):
        for player in self.__players:
            while player.action(self) == Action.HIT:
                self.__hands[player].add(self.__deck.next())

        while self.__dealer_hand.score() < 17:
            self.__dealer_hand.add(self.__deck.next())

        self.__finished = True

    def get_players(self):
        return self.__players

    def get_player_hand(self, player):
        if not self.__initialized:
            raise GameIsNotInitializedException()
        return self.__hands[player]

    def get_dealer_up_card(self):
        if not self.__initialized:
            raise GameIsNotInitializedException()
        return self.__dealer_hand.get(0)

    def get_dealer_hand(self):
        if not self.__initialized:
            raise GameIsNotInitializedException()

        if not self.__finished:
            raise GameIsNotFinishedException()

        return self.__dealer_hand

    def show_result(self):
        print("Dealer", end=",")
        for card in self.__dealer_hand.cards:
            print(card, end=",")
        print("")
        for player in self.__players:
            hand = self.get_player_hand(player)
            print(player.get_name(), end=",")
            print(Hand.check(hand, self.__dealer_hand), end=",")
            for card in hand.cards:
                print(card, end=",")
            print("")

