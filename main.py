from sources import GameMatrix

game_matrix = GameMatrix()
game_matrix.init_winning_probs()
probs_df = game_matrix.probs_to_df()
(probs_df.to_csv("winning_probs.csv"))
print(probs_df)
print(game_matrix.get_win_prob(0, 3))
print(game_matrix.get_result_prob(0, 0, "draw"))
