import random

from sources.strategy import Strategy


class ExpectationEval(Strategy):
    def __init__(self, player) -> None:
        super().__init__(player)

    def create_subset(self):
        subset = ["N"]
        self.get_game_matrix().init_winning_probs(count_draws=True)
        best_strat_index = self.get_game_matrix().winning_probs.mean(axis=1).argmax()
        best_strat = self.get_game_matrix().strategy_table[best_strat_index]
        print(f"Best strat: {best_strat}")
        subset = ["N"]
        for _ in range(1, self.get_game().subset_size):
            subset.append(best_strat)
        self.player.subset = subset
