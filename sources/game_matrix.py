import numpy  as np
import pandas as pd

class GameMatrix:
    def __init__(self):
        
        self.strategy_table = ['W', 'S', 'G', 'E', 'M', 'T', 'N']
        self.n_strategies = len(self.strategy_table)
        self.winnging_probs = np.zeros((self.n_strategies, self.n_strategies))
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
    
    def init_winning_probs(self):
        for i in range(self.n_strategies):
            for j in range(self.n_strategies):
                dice_1 = self.dice_matrix[i][j]
                dice_2 = self.dice_matrix[j][i]
                biggest = max(dice_1, dice_2)
                smallest = min(dice_1, dice_2)
                #print(5*'-')
                #print(f'{smallest} vs {biggest}')
                smallest_wins_prob = (smallest - 1) / (biggest *2)
                draw_prob = 1 / biggest
                #print(f'{smallest_wins_prob:.2f}, draw: {draw_prob:.2f}')
                if(dice_1 == dice_2):
                    self.winnging_probs[i][j] = (1 - draw_prob) / 2
                elif(dice_1 < dice_2):
                    self.winnging_probs[i][j] = smallest_wins_prob 
                else:
                    self.winnging_probs[i][j] = 1 - smallest_wins_prob - draw_prob
                #print(f'winning prob: {self.winnging_probs[i][j]:.2f} , {1-draw_prob:.2f}')
                self.winnging_probs[i][j] = self.winnging_probs[i][j] / (1-draw_prob)

    def get_dice_with_strategy(self, strategy_1:str, strategy_2:str):
        return self.dice_matrix[self.strategy_to_index[strategy_1]][self.strategy_to_index[strategy_2]]
    
    def get_dice_with_index(self, index_1:int, index_2:int):
        return self.dice_matrix[index_1][index_2]
    
    def generate_df(self):
        dice_format = lambda n_dice: f'D{n_dice}'
        df=  pd.DataFrame(self.dice_matrix, columns=self.strategy_table, index=self.strategy_table)
        df = df.map(dice_format)
        return df
    
    def probs_to_df(self):
        df = pd.DataFrame(self.winnging_probs, columns=self.strategy_table, index=self.strategy_table)
        return df
    
    
