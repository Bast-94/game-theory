import random

from sources.game import Game


class Player:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.score = 0
        self.strategy = None
        self.subset = ["N"]
        self.played_strategy = None
        if self.strategy is None:
            for i in range(1, self.game.subset_size):
                self.subset.append(random.choice(self.game.game_matrix.strategy_table))

    def choice_strategy(self):
        # pop random strategy from subset
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
