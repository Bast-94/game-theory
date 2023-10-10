import random

from sources.default_strategy import DefaultStrategy
from sources.game import Game
from sources.strategy import Strategy


class Player:
    def __init__(self, game: Game, strat_algo: Strategy = None) -> None:
        self.game = game
        self.score = 0
        self.strat_algo = DefaultStrategy(self) if strat_algo is None else strat_algo
        self.played_strategy = None
        self.subset = None
        self.strat_algo.create_subset()

    def choice_strategy(self):
        chosen_strategy = random.choice(self.subset)
        return chosen_strategy

    def play_strategy(self):
        self.played_strategy = self.choice_strategy()
        dice = self.game.game_matrix.get_dice_with_strategy(
            self.played_strategy, self.played_strategy
        )
        score = random.randint(1, dice + 1)
        self.score += score
        return score

    def remove_strategy(self):
        self.subset.remove(self.played_strategy)
