from sources.player import Player


class StratAlgo:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.game_matrix = player.game.game_matrix
    
    def get_subset(self):
        return self.player.subset

    def get_subset_size(self, player: Player):
        return len(self.get_subset())
    
    def choice(self, player: Player):
        return self.get_subset()[0]
    