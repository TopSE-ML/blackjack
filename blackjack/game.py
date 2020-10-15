from blackjack.action import Action
from blackjack.hand import Hand


class GameIsNotInitializedException(Exception):
    pass


class GameIsNotFinishedException(Exception):
    pass


class Game:

    def __init__(self):
        self.initialized = False
        self.finished = False
        self.deck = None
        self.players = []
        self.hands = dict()
        self.dealer_hand = Hand()

    def is_initialized(self):
        return self.initialized

    def setup(self, deck, players):
        self.initialized = True
        self.deck = deck
        for player in players:
            self.players.append(player)
            hand = Hand()
            hand.add(self.deck.next())
            hand.add(self.deck.next())
            self.hands[player] = hand
        self.dealer_hand.add(self.deck.next())
        self.dealer_hand.add(self.deck.next())

    def play(self):
        for player in self.players:
            while player.action(self) == Action.HIT:
                self.hands[player].add(self.deck.next())

        while self.dealer_hand.score() < 17:
            self.dealer_hand.add(self.deck.next())

        self.finished = True

    def get_player_hand(self, player):
        if not self.initialized:
            raise GameIsNotInitializedException()
        return self.hands[player]

    def get_dealer_up_card(self):
        if not self.initialized:
            raise GameIsNotInitializedException()
        return self.dealer_hand.get(0)

    def get_dealer_hand(self):
        if not self.initialized:
            raise GameIsNotInitializedException()

        if not self.finished:
            raise GameIsNotFinishedException()

        return self.dealer_hand

    def show_result(self):
        print("Dealer", end=",")
        for card in self.dealer_hand.cards:
            print(card, end=",")
        print("")
        for player in self.players:
            hand = self.get_player_hand(player)
            print(player.get_name(), end=",")
            print(Hand.check(hand, self.dealer_hand), end=",")
            for card in hand.cards:
                print(card, end=",")
            print("")

