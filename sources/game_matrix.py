import random

import numpy as np
import pandas as pd


class GameMatrix:
    """
    A class representing the game matrix for a game of dice.

    Attributes:
    -----------
    strategy_table : list
        A list of strings representing the available strategies for the game.
    n_strategies : int
        The number of strategies available in the game.
    winnging_probs : numpy.ndarray
        A 2D numpy array representing the winning probabilities for each pair of strategies.
    dice_matrix : numpy.ndarray
        A 2D numpy array representing the dice roll probabilities for each pair of strategies.
    index_to_strategy : dict
        A dictionary mapping strategy indices to their corresponding string representation.
    strategy_to_index : dict
        A dictionary mapping strategy string representations to their corresponding index.
    """

    def __init__(self):
        """
        Initializes the GameMatrix object with default values for the game matrix.
        """
        self.strategy_table = ["W", "S", "G", "E", "M", "T", "N"]
        self.n_strategies = len(self.strategy_table)
        self.winning_probs = np.zeros((self.n_strategies, self.n_strategies))
        dice_matrix = [
            [6, 10, 6, 12, 10, 3, 4],
            [6, 6, 3, 6, 6, 12, 4],
            [6, 12, 6, 4, 6, 10, 3],
            [3, 4, 6, 6, 12, 4, 6],
            [10, 6, 12, 3, 6, 6, 4],
            [6, 4, 10, 10, 6, 3, 12],
            [12, 10, 10, 3, 4, 6, 6],
        ]
        self.dice_matrix = np.array(dice_matrix)
        self.index_to_strategy = {
            i: self.strategy_table[i] for i in range(len(self.strategy_table))
        }
        self.strategy_to_index = {
            self.strategy_table[i]: i for i in range(len(self.strategy_table))
        }

    def init_winning_probs(self, count_draws=False):
        for i in range(self.n_strategies):
            for j in range(self.n_strategies):
                self.winning_probs[i][j] = self.get_win_prob(i, j)
                if count_draws:
                    self.winning_probs[i][j] += self.get_result_prob(i, j, "draw")

    def get_win_prob(self, strategy_1: str | int, strategy_2: str | int):
        return self.get_result_prob(strategy_1, strategy_2, "win")

    def get_result_prob(
        self, strategy_1: str | int, strategy_2: str | int, result_type: str
    ):
        assert result_type in ["win", "draw", "lose"]
        if isinstance(strategy_1, str) and isinstance(strategy_2, str):
            strategy_1 = self.strategy_to_index[strategy_1]
            strategy_2 = self.strategy_to_index[strategy_2]
        dice_1 = self.dice_matrix[strategy_1, strategy_2]
        dice_2 = self.dice_matrix[strategy_2, strategy_1]
        draw_prob = 1 / max(dice_1, dice_2)
        if result_type == "draw":
            return draw_prob
        winning_prob = 0
        if dice_1 == dice_2:
            winning_prob = (1 - 1 / dice_1) / 2
        elif dice_1 < dice_2:
            winning_prob = (dice_1 - 1) / (dice_2 * 2)
        else:
            winning_prob = 1 - (dice_2 - 1) / (dice_1 * 2) - draw_prob
        if result_type == "win":
            return winning_prob
        return 1 - winning_prob - draw_prob

    def get_dice_with_strategy(self, strategy_1: str, strategy_2: str):
        return self.dice_matrix[self.strategy_to_index[strategy_1]][
            self.strategy_to_index[strategy_2]
        ]

    def get_dice_with_index(self, index_1: int, index_2: int):
        return self.dice_matrix[index_1][index_2]

    def generate_df(self):
        dice_format = lambda n_dice: f"D{n_dice}"
        df = pd.DataFrame(
            self.dice_matrix, columns=self.strategy_table, index=self.strategy_table
        )
        df = df.map(dice_format)
        return df

    def probs_to_df(self):
        df = pd.DataFrame(
            self.winning_probs, columns=self.strategy_table, index=self.strategy_table
        )
        return df

    def get_score(self, strategy_1: str, strategy_2: str):
        if isinstance(strategy_1, str) and isinstance(strategy_2, str):
            strategy_1 = self.strategy_to_index[strategy_1]
            strategy_2 = self.strategy_to_index[strategy_2]
        dice_1 = self.dice_matrix[strategy_1, strategy_2]
        return random.randint(1, dice_1 + 1)
