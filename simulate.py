from sources import (DefaultStrategy, ExpectationEval, Game, GameMatrix,
                     Player, Strategy)

player_1 = Player(Game(), ExpectationEval)
game = Game(player_1=player_1)
game.render()
game_matrix = game.game_matrix
game_matrix.init_winning_probs()

print(game_matrix.probs_to_df())
game.run()
print(game.winner)
