
class Strategy:
    
    def __init__(self, player) -> None:
        self.player = player
        self.game_matrix = player.game.game_matrix
    def get_subset(self):
        return self.player.subset

    def get_subset_size(self):
        return len(self.get_subset())

    def choice(self):
        pass
    
    def create_subset(self):
        pass
