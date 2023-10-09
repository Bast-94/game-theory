from sources import GameMatrix
game_matrix = GameMatrix()
game_matrix.init_winning_probs()
(game_matrix.probs_to_df().to_csv('winning_probs.csv'))