from sources import Game


class Player:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.score = 0
