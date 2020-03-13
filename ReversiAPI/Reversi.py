from Board import Field, Grid

class Game:
    def __init__(self, token, playerBlack, playerWhite):
        self.token = token
        self.black = playerBlack
        self.white = playerWhite
        self.turn = playerBlack
        self.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.board = Grid(self.columns)

    def addGrid(self, grid):
        for row in self.board.grid:
            for field in row:
                i = field.row-1
                c = self.columns.index(field.col)
                field.playedBy = grid[i][c]

    @property
    def playerValue(self):
        return 1 if self.turn == self.white else -1

    @property 
    def opponentValue(self):
        return 1 if self.playerValue == -1 else -1

    def __str__(self):
        gameDict = {}
        gameDict['gameToken'] = self.token
        gameDict['gameGrid'] = str(self.board)
        return str(gameDict).replace("'", '"')

    def set(self, row, col, value):
        """Set field value in field in grid
        
        Arguments:
            row {int} -- row number
            col {string} -- column name
            value {int} -- -1 for black, 1 for white, 0 for neither
        """
        self.board.set(row, col, value)

    def get(self, row, col):
        """Get field value in grid
        
        Arguments:
            row {int} -- row numner
            col {string} -- column name

        Returns:
            int -- Value of field
        """
        return self.board.get(row, col).playedBy

    def addPlayer(self, newPlayerToken):
        """Add new played togame
        
        Arguments:
            newPlayerToken {string} -- playertoken
        """
        if self.black is None:
            self.black = newPlayerToken
        elif self.white is None:
            self.white = newPlayerToken
        else:
            raise("Something is wrong here.")

    def update(self, playerToken, row, col):
        """Updates the grid when a move is made
        
        Arguments:
            playerToken {string} -- Token of the player who made the move
            row {int} -- Row in which the move was done
            col {str} -- Column in which the move was done
        
        Returns:
            bool -- True if move went through, False if it didn't
        """
        try:
            if (playerToken == self.turn and self.legalMove(row, col)):
                self.flipValues(row, col)
                if (playerToken == self.black):
                    self.turn = self.white
                elif(playerToken == self.white):
                    self.turn = self.black
                else:
                    raise('Something went wrong')
            else:
                raise('Illegal move')
            return True
        except Exception as exception:
            return False

    def legalMove(self, row, col):
        """Checks wether a move is legal or not
        
        Arguments:
            row {int} -- Row in which the move was made
            col {str} -- Column which the move was made in
        
        Returns:
            Boolean -- True if move is legal
        """
        col = col.lower()
        rowIdx = row - 1
        colIdx = self.columns.index(col)
        if (self.get(row, col) == 0):
            surroundingValues = [
                # row above desired field to fill
                self.getFieldValue(rowIdx - 1, colIdx - 1), self.getFieldValue(rowIdx - 1, colIdx), self.getFieldValue(rowIdx - 1, colIdx + 1),
                # row at desired field to fill
                self.getFieldValue(rowIdx, colIdx - 1),                                             self.getFieldValue(rowIdx, colIdx + 1),
                # row below desired field to fill
                self.getFieldValue(rowIdx + 1, colIdx - 1), self.getFieldValue(rowIdx + 1, colIdx), self.getFieldValue(rowIdx + 1, colIdx + 1)
            ]
            return any(x == 1 or x == -1 for x in surroundingValues)
        else: # user tries to fill field that's already filled
            return False

    def getFieldValue(self, rowIdx, colIdx):
        """Returns the played value of a field based on row Index and Column index
        !!Look out!!

        Arguments:
            rowIdx {int} -- row index
            colIdx {int} -- column index
        
        Returns:
            Field -- Field of grind in requested row index and column index.
        """
        if ( rowIdx < 0 or rowIdx > 7 or colIdx < 0 or colIdx > 7 ): # out of bounds
            return 0
        else:
            col = self.columns[colIdx]
            return self.get(rowIdx+1, col)

    
    def flipValues(self, row, col):
        """Flips the values after a legal move came throufh
        
        Arguments:
            row {int} -- Row of the move resulting in the flippin'
            col {str} -- Col of the move resulting in the flippin'
        """
        playerValue = 1 if self.turn == self.white else -1

        self.set(row, col, playerValue)
        self.flipHorizontal_Left(row, col)
        self.flipHorizontal_Right(row, col)
        self.flipVertical_top(row, col)
        self.flipVertical_bot(row, col)
        self.flipDiagonal_topLeft(row, col)
        self.flipDiagonal_topRight(row, col)
        self.flipDiagonal_botLeft(row, col)
        self.flipDiagonal_botRight(row, col)

    def flipHorizontal_Left(self, row, col):
        """Flips stones left of the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col
        """
        currentColIdx = self.columns.index(col)
        nextColIdx = currentColIdx - 1

        if (self.board.get(row, self.columns[nextColIdx]).playedBy != 0): #has stone to te left
            #search for own stone
            playerStoneFount = False
            fieldsToFlip = []
            while (nextColIdx >= 0):
                nextField = self.board.get(row, self.columns[nextColIdx])
                if (nextField.playedBy == self.playerValue):
                    playerStoneFount = True
                    break
                fieldsToFlip.append(self.board.get(row, self.columns[nextColIdx]))
                currentColIdx = nextColIdx
                nextColIdx-=1

            if (playerStoneFount): #flip values
                for field in fieldsToFlip:
                    field.playedBy = self.playerValue

    def flipHorizontal_Right(self, row, col):
        """Flips stones right of the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col
        """
        currentColIdx = self.columns.index(col)
        nextColIdx = currentColIdx + 1
        if nextColIdx < len(self.columns):
            if (self.board.get(row, self.columns[nextColIdx]).playedBy != 0): #has stone to the right
                playerStoneFount = False
                fieldsToFlip = []
                while (nextColIdx < len(self.columns)):
                    nextField = self.board.get(row, self.columns[nextColIdx])
                    if (nextField.playedBy == self.playerValue):
                        playerStoneFount = True
                        break
                    fieldsToFlip.append(self.board.get(row, self.columns[nextColIdx]))
                    currentColIdx = nextColIdx
                    nextColIdx += 1
                if playerStoneFount:
                    for field in fieldsToFlip:
                        field.playedBy = self.playerValue

    def flipVertical_top(self, row, col):
        """Flips stones above the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col
        """
        columnArray = []
        for r in self.board.grid:
            for field in r:
                if field.col == col:
                    columnArray.append(field)

        currentField = columnArray[row - 1]
        nextFieldIdx = row - 2
        nextField = columnArray[nextFieldIdx]

        if (nextField.playedBy != 0): # has stone above it
            playerStoneFount = False
            fieldsToFlip = []
            while(nextFieldIdx > 0):
                if (nextField.playedBy == self.playerValue):
                    playerStoneFount = True
                    break
                fieldsToFlip.append(nextField)
                currentField = nextField
                nextField = columnArray[nextFieldIdx - 1]
                nextFieldIdx-=1
            if (playerStoneFount):
                for field in fieldsToFlip:
                    field.playedBy = self.playerValue
        

    def flipVertical_bot(self, row, col):
        """Flips stones belowthe move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col
        """
        columnArray = []
        for r in self.board.grid:
            for field in r:
                if field.col == col:
                    columnArray.append(field)
        # loop through collumn
        currentField = columnArray[row - 1]
        nextFieldIdx = row
        nextField = columnArray[nextFieldIdx]

        if (nextField.playedBy != 0):
            playerStoneFount = False
            fieldsToFlip = []
            while (nextFieldIdx < len(columnArray)):
                if (nextField.playedBy == self.playerValue):
                    playerStoneFount = True
                    break
                fieldsToFlip.append(nextField)
                currentField = nextField
                nextField = columnArray[nextFieldIdx + 1]
                nextFieldIdx+=1
            if (playerStoneFount):
                for field in fieldsToFlip:
                    field.playedBy = self.playerValue

    def flipDiagonal_topLeft(self,row,col):
        """Flips stones top left of the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col
        """
        # alle rijen boven row checken
        # alle cols rechts van col checken
        fields = []
        row = row - 1
        colIdx = self.columns.index(col) - 1
        for ri in range(row, 0, -1):
            try:
                fields.append(self.board.get(ri, self.columns[colIdx]))
                colIdx-=1
            except IndexError:
                break
        self.fieldsTest(fields)
        pass

    def flipDiagonal_topRight(self,row,col):
        """Flips stones top right of the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col
        """
        # alle rijen boven row checken
        # alle cols rechts van col checken
        fields = []
        row = row - 1 
        colIdx = self.columns.index(col) + 1
        for ri in range(row, 0, -1):
            try:
                fields.append(self.board.get(ri, self.columns[colIdx]))
                colIdx+=1
            except IndexError:
                break
                
        self.fieldsTest(fields)
        

    def flipDiagonal_botLeft(self,row,col):
        """Flips stones bot left of the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col
        """
        fields = []
        row = row + 1
        colIdx = self.columns.index(col) - 1

        for ri in range(row, len(self.columns) + 1, 1):
            try:
                fields.append(self.board.get(ri, self.columns[colIdx]))
                colIdx-=1
            except IndexError:
                break

        self.fieldsTest(fields)

    def flipDiagonal_botRight(self,row,col):
        """Flips stones bot right of the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col
        """
        fields = []
        row = row + 1
        colIdx = self.columns.index(col) + 1

        for ri in range(row, len(self.columns) + 1, 1):
            try:
                fields.append(self.board.get(ri, self.columns[colIdx]))
                colIdx+=1
            except IndexError:
                break

        self.fieldsTest(fields)

    def fieldsTest(self, fields):
        i = 0
        fieldsToFlip = []
        playerStoneFount = False
        if (fields[i].playedBy != 0): #checks if field top right is filled
            for field in fields:
                if (i == len(fields) - 1): # hit wall
                    break
                fieldsToFlip.append(field)
                if (fields[i+1].playedBy == self.playerValue):
                    playerStoneFount = True
                    break
                i+=1

        if playerStoneFount:
            for field in fieldsToFlip:
                field.playedBy = self.playerValue
