import random

from sources.game_matrix import GameMatrix


class Game:
    def __init__(self) -> None:
        from sources.player import Player

        self.game_matrix = GameMatrix()
        self.game_matrix.init_winning_probs()
        self.subset_size = 10
        self.player_1 = Player(self)
        self.player_2 = Player(self)
        self.winner = None

    def render(self):
        print("Player 1: ", self.player_1.score)
        print("Player 2: ", self.player_2.score)
        print("Player 1 subset: ", self.player_1.subset)
        print("Player 2 subset: ", self.player_2.subset)

    def buy_phase(self):
        pass

    def dual_phase(self):
        player_1_score = self.player_1.play_strategy()
        player_2_score = self.player_2.play_strategy()

        if player_1_score > player_2_score:
            print("Player 1 win")
            self.player_2.remove_strategy()

        elif player_1_score < player_2_score:
            print("Player 2 win")
            self.player_1.remove_strategy()

    def check_win_phase(self):
        stop_game = not ("N" in self.player_1.subset) or not (
            "N" in self.player_2.subset
        )

        return stop_game

    def run(self):
        while not self.check_win_phase():
            self.buy_phase()
            self.dual_phase()
