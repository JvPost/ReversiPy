class Game:
    def __init__(self, token, playerBlack, playerWhite):
        self.token = token
        self.black = playerBlack
        self.white = playerWhite
        self.turn = playerBlack
        self.grid = {
                "A": [0, 0, 0, 0, 0, 0, 0, 0],
                "B": [0, 0, 0, 0, 0, 0, 0, 0],
                "C": [0, 0, 0, 0, 0, 0, 0, 0],
                "D": [0, 0, 0, 1,-1, 0, 0, 0],
                "E": [0, 0, 0,-1, 1, 0, 0, 0],
                "F": [0, 0, 0, 0, 0, 0, 0, 0],
                "G": [0, 0, 0, 0, 0, 0, 0, 0],
                "H": [0, 0, 0, 0, 0, 0, 0, 0],
            }

    def __str__(self):
        gameDict = {}
        gameDict['gameToken'] = self.token
        gameDict['gameGrid'] = self.grid
        return str(gameDict).replace("'", '"')

    def addPlayer(self, newPlayerToken):
        if self.black is None:
            self.black = newPlayerToken
        elif self.white is None:
            self.white = newPlayerToken
        else:
            raise("Something is wrong here.")

    def update(self, playerToken, row, col):
        try:
            newGridValue = 0
            if (playerToken == self.white and self.turn == self.white):
                newGridValue = 1
                self.turn = self.black
            elif(playerToken == self.black and self.turn == self.black):
                self.turn = self.white
                newGridValue = -1
            else:
                raise('Illegal move')
            self.grid[col][row - 1] = newGridValue
            return True
        except:
            return False

