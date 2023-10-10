from sources.strategy import Strategy


class ExpectationEval(Strategy):
    def __init__(self, player) -> None:
        super().__init__(player)

    def create_subset(self):
        subset = ["N"]
        self.game_matrix.init_winning_probs()
        best_strat_index = self.game_matrix.winning_probs.mean(axis=1).argmax()
