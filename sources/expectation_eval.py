import random

from sources.strategy import Strategy


class ExpectationEval(Strategy):
    name = "ExpectationEval"

    def __init__(self, player) -> None:
        super().__init__(player)

    def choice(self):
        # return a value different from 'N' if the subset is not empty

        for strat in self.get_subset():
            if strat != "N" and len(self.get_subset()) > 1:
                return strat
            else:
                return strat

    def create_subset(self):
        subset = ["N"]
        self.get_game_matrix().init_winning_probs(count_draws=True)
        best_strat_index = self.get_game_matrix().winning_probs.mean(axis=1).argmax()
        best_strat = self.get_game_matrix().strategy_table[best_strat_index]

        for _ in range(1, self.get_game().subset_size):
            subset.append(best_strat)
        self.player.subset = subset
