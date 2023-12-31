import random

from sources.strategy import Strategy


class RandomStrategy(Strategy):
    name = "Random"

    def __init__(self, player) -> None:
        super().__init__(player)

    def choice(self):
        return random.choice(self.get_subset())

    def create_subset(self):
        subset = ["N"]
        for _ in range(1, self.player.game.subset_size):
            subset.append(random.choice(self.get_game_matrix().strategy_table))
        self.player.subset = subset
