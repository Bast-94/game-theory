from sources import (DefaultStrategy, ExpectationEval, Game, GameMatrix,
                     Player, Strategy)

nb_simulations = 1000
counter = 0
for _ in range(nb_simulations):
    player_1 = Player(Game(), ExpectationEval)
    game = Game(player_1=player_1, verbose=False)
    game.run()
    if game.winner == player_1:
        counter += 1
print(f"Player 1 won {counter} times out of {nb_simulations} simulations")
