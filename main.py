from sources import GameMatrix

game_matrix = GameMatrix()
game_matrix.init_winning_probs()
probs_df = game_matrix.probs_to_df()
(probs_df.to_csv("winning_probs.csv"))
print(probs_df)
