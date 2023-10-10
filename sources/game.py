from sources import GameMatrix


class Game:
    def __init__(self) -> None:
        self.game_matrix = GameMatrix()
        self.game_matrix.init_winning_probs()

    def buy_phase(self):
        pass

    def dual_phase(self):
        pass

    def check_win_phase(self):
        pass
