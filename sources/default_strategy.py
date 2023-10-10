from sources.strategy import Strategy

import random

class DefaultStrategy(Strategy):
    
    def __init__(self, player) -> None:
        super().__init__(player)
    

    def choice(self):
        pass
    
    def create_subset(self):
        subset = ["N"]
        for _ in range(1, self.game_matrix.n_strategies):
            subset.append(random.choice(self.game_matrix.strategy_table))
        self.player.subset = subset