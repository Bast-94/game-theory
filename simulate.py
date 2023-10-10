from itertools import product

from sources import (ExpectationEval, Game, GameMatrix, Player, RandomStrategy,
                     Strategy)

nb_simulations = 1000
counter = 0

strategies = [RandomStrategy, ExpectationEval]
parameters = {
    "player_1_strategy": strategies,
    "player_2_strategy": strategies,
}


def gen_list_of_dicts(dict_with_lists):
    # Utilisez product pour obtenir une liste de dictionnaires
    list_of_dicts = [
        dict(zip(dict_with_lists.keys(), values))
        for values in product(*dict_with_lists.values())
    ]
    return list_of_dicts


def make_simulations(nb_simulations, player_1_strategy, player_2_strategy):
    counter_1 = 0
    counter_2 = 0
    print(
        f"Simulating {nb_simulations} games with {player_1_strategy.name} vs {player_2_strategy.name}"
    )
    for _ in range(nb_simulations):
        player_1 = Player(Game(), player_1_strategy)
        player_2 = Player(Game(), player_2_strategy)
        game = Game(player_1=player_1, player_2=player_2, verbose=False)
        game.run()
        if game.winner == player_1:
            counter_1 += 1
        if game.winner == player_2:
            counter_2 += 1

    print(f"Player 1 won {counter_1} times and player 2 won {counter_2} times")
    return counter_1, counter_2


parameters_combinations = gen_list_of_dicts(parameters)
for paramater in parameters_combinations:
    make_simulations(nb_simulations, **paramater)
