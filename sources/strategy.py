import random


class Strategy:
    def __init__(self, player) -> None:
        self.name = "Default"
        self.player = player

    def get_subset(self):
        return self.player.subset

    def get_subset_size(self):
        return len(self.get_subset())

    def choice(self):
        return random.choice(self.get_subset())

    def get_game_matrix(self):
        return self.player.game.game_matrix

    def get_game(self):
        return self.player.game

    def create_subset(self):
        pass

    def buy_items(self):
        pass
