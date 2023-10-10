import random

from sources.game import Game


class Player:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.score = 0
        self.strategy = None
        self.subset = ["N"]
        if self.strategy is None:
            for i in range(1, self.game.subset_size):
                self.subset.append(random.choice(self.game.game_matrix.strategy_table))
