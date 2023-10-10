import numpy as np

from sources import GameMatrix

game_matrix = GameMatrix()
game_matrix.init_winning_probs()
mat = game_matrix.dice_matrix - game_matrix.dice_matrix.T
print(mat)
print(mat[np.where(mat > 0)])
