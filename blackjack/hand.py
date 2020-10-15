class Hand:

    def __init__(self):
        self.cards = []

    @staticmethod
    def __expand_candidates(scores, candidates):
        result = []
        for score in scores:
            for v in candidates:
                result.append(score + v)
        return result

    @staticmethod
    def __choose_best_score(candidates):
        candidates = sorted(candidates, reverse=True)
        valid = list(filter(lambda s: s <= 21, candidates))

        if len(valid) == 0:
            return min(candidates)
        else:
            return max(valid)

    def score(self):
        candidates = [0]
        for card in self.cards:
            score = card.score()
            if type(score) is list:
                candidates = self.__expand_candidates(score, candidates)
            else:
                candidates = [ v + score for v in candidates ]

        return self.__choose_best_score(candidates)

    def add(self, card):
        self.cards.append(card)

    def get(self, index):
        return self.cards[index]

    def is_blackjack(self):
        return True if self.score() == 21 and len(self.cards) == 2 else False

    def is_bust(self):
        return self.score() > 21

    @staticmethod
    def check(player, dealer):
        player_score = player.score()
        dealer_score = dealer.score()

        if player.is_bust():
            return "LOSE"

        if dealer.is_bust():
            return "WIN"

        if player.is_blackjack() and not dealer.is_blackjack():
            return "WIN"

        if not player.is_blackjack() and dealer.is_blackjack():
            return "LOSE"

        if player_score == dealer_score:
            return "DRAW"

        return "WIN" if player_score > dealer_score else "LOSE"
