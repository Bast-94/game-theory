from sources import Game, GameMatrix, Player

game = Game()
game.render()
game_matrix = GameMatrix()
game_matrix.init_winning_probs()
print(game_matrix.probs_to_df())
