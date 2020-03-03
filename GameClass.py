class Game:
    def __init__(self, token, playerWhite, playerBlack):
        self.token = token
        self.white = playerWhite
        self.black = playerBlack
        self.grid = {
                "A": [0,0,0,0,0,0,0],
                "B": [0,0,0,0,0,0,0],
                "C": [0,0,0,0,0,0,0],
                "D": [0,0,0,0,0,0,0],
                "E": [0,0,0,0,0,0,0],
                "F": [0,0,0,0,0,0,0],
                "G": [0,0,0,0,0,0,0],
                "H": [0,0,0,0,0,0,0],
            }


