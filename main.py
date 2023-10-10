import numpy as np

from sources import GameMatrix

game_matrix = GameMatrix()
game_matrix.init_winning_probs()
mat = game_matrix.dice_matrix - game_matrix.dice_matrix.T
print(mat)
couples = np.array(np.where(mat > 0))
couples = couples.T
print(couples)
for a, b in couples:
    print(game_matrix.strategy_table[a], ">", game_matrix.strategy_table[b])

    print("----")
