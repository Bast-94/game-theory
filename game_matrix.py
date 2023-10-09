import numpy  as np


class GameMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.strategy_table = ['W', 'S', 'G', 'E', 'M', 'T', 'N']
        self.dice_matrix = np.zeros((len(self.strategy_table), len(self.strategy_table)))
        self.index_to_strategy = {i: self.strategy_table[i] for i in range(len(self.strategy_table))}
        self.strategy_to_index = {self.strategy_table[i]: i for i in range(len(self.strategy_table))}

    def get_dice_with_strategy(self, strategy_1:str, strategy_2:str):
        return self.matrix[self.strategy_to_index[strategy_1]][self.strategy_to_index[strategy_2]]
    