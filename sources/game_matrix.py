import numpy  as np
import pandas as pd

class GameMatrix:
    def __init__(self):
        
        self.strategy_table = ['W', 'S', 'G', 'E', 'M', 'T', 'N']
        dice_matrix = [ [6, 10, 6, 12, 10, 3, 4],
            [6, 6, 3, 6, 6, 12, 4],
            [6, 12, 6, 4, 6,10, 3],
            [3, 4, 6, 6, 12, 4, 6],
            [10, 6, 12, 3, 6, 6, 4],
            [6, 4, 10, 10, 6, 3, 12],
            [12, 10, 10, 3, 4, 6, 6]]
        self.dice_matrix = np.array(dice_matrix)
        self.index_to_strategy = {i: self.strategy_table[i] for i in range(len(self.strategy_table))}
        self.strategy_to_index = {self.strategy_table[i]: i for i in range(len(self.strategy_table))}

    def get_dice_with_strategy(self, strategy_1:str, strategy_2:str):
        return self.dice_matrix[self.strategy_to_index[strategy_1]][self.strategy_to_index[strategy_2]]
    
    def get_dice_with_index(self, index_1:int, index_2:int):
        return self.dice_matrix[index_1][index_2]
    
    def generate_df(self):
        dice_format = lambda n_dice: f'D{n_dice}'
        df=  pd.DataFrame(self.dice_matrix, columns=self.strategy_table, index=self.strategy_table)
        df = df.map(dice_format)
        return df
    
