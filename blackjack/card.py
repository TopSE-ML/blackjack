from enum import Enum


class Card(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def score(self):
        if self == Card.ACE:
            return [1, 11]
        elif self in [Card.JACK, Card.QUEEN, Card.KING]:
            return 10
        else:
            return self.value

    def __str__(self):
        return self.name