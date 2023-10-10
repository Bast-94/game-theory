import random

from sources.game_matrix import GameMatrix


class Game:
    def __init__(self, player_1=None, player_2=None) -> None:
        from sources.player import Player

        self.game_matrix = GameMatrix()
        self.game_matrix.init_winning_probs()
        self.subset_size = 10
        self.player_1 = Player(self) if player_1 is None else player_1
        self.player_1.game = self
        self.player_2 = Player(self) if player_2 is None else player_2
        self.player_2.game = self
        self.winner = None

    def render(self):
        print("Player 1: ", self.player_1.score)
        print("Player 2: ", self.player_2.score)
        print("Player 1 subset: ", self.player_1.subset)
        print("Player 2 subset: ", self.player_2.subset)

    def buy_phase(self):
        pass

    def dual_phase(self):
        print("Payer 1 subset: ", self.player_1.subset)
        print("Payer 2 subset: ", self.player_2.subset)
        self.player_1.play_strategy()
        self.player_2.play_strategy()
        print("Player 1 played: ", self.player_1.played_strategy)
        print("Player 2 played: ", self.player_2.played_strategy)
        strat_1 = self.player_1.played_strategy
        strat_2 = self.player_2.played_strategy
        print("Strat 1: ", strat_1)

        player_1_score = self.game_matrix.get_score(strat_1, strat_2)
        player_2_score = self.game_matrix.get_score(strat_2, strat_1)

        print("Player 1 score: ", player_1_score)
        print("Player 2 score: ", player_2_score)

        if player_1_score > player_2_score:
            print("Player 1 win")
            self.player_2.remove_strategy()

        elif player_1_score < player_2_score:
            print("Player 2 win")
            self.player_1.remove_strategy()
        else:
            print("Draw")

    def check_win_phase(self):
        stop_game = not ("N" in self.player_1.subset) or not (
            "N" in self.player_2.subset
        )

        return stop_game

    def run(self):
        while not self.check_win_phase():
            self.buy_phase()
            self.dual_phase()
