import random

from sources.default_strategy import DefaultStrategy
from sources.game import Game
from sources.strategy import Strategy


class Player:
    def __init__(self, game: Game, strat_algo_class=None) -> None:
        self.game = game
        self.score = 0
        self.strat_algo = (
            DefaultStrategy(self)
            if strat_algo_class is None
            else strat_algo_class(self)
        )
        self.played_strategy = None
        self.subset = None
        self.strat_algo.create_subset()

    def choice_strategy(self):
        return self.strat_algo.choice()

    def play_strategy(self):
        self.played_strategy = self.choice_strategy()

    def remove_strategy(self):
        self.subset.remove(self.played_strategy)
