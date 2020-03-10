class Game:
    def __init__(self, token, playerBlack, playerWhite):
        self.token = 'token' # TODO set token
        self.black = playerBlack
        self.white = playerWhite
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


    def update(self, playerToken, row, col):
        newGridValue = 0
        if (playerToken == self.white):
            newGridValue = 1
        elif(playerToken == self.black):
            newGridValue = -1
        else:
            raise('NO')
        self.grid[col][row - 1] = newGridValue

