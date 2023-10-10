from sources import GameMatrix

game_matrix = GameMatrix()
game_matrix.init_winning_probs()
print(game_matrix.winning_probs.mean(axis=1))
print(game_matrix.winning_probs)
# game_matrix.winning_probs
