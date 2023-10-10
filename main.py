from sources import GameMatrix

game_matrix = GameMatrix()
game_matrix.init_winning_probs()
print(game_matrix.dice_matrix - game_matrix.dice_matrix.T)
