from Board import Field, Grid, CanBePlayedBy, FieldValue


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
                if grid[i][c] == FieldValue.BLACK.value:
                    field.playedBy = FieldValue.BLACK
                elif grid[i][c] == FieldValue.WHITE.value:
                    field.playableBy = FieldValue.WHITE
                else:
                    field.playableBy = FieldValue.NONE
                    

    @property
    def playerValue(self):
        return FieldValue.WHITE if self.turn == self.white else FieldValue.BLACK

    @property 
    def opponentValue(self):
        return FieldValue.WHITE if self.playerValue == FieldValue.BLACK else FieldValue.BLACK

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
            value {FieldValue} -- -1 for black, 1 for white, 0 for neither
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
            if (playerToken == self.turn and self.checkBorderedToStone(row, col)):
                self.flipValues(row, col)
            else:
                raise('Illegal move')
            return True
        except Exception as exception:
            return False


    ### ####################################### ###
    ###             Helpers                     ###
    ### ####################################### ###
    def checkBorderedToStone(self, row, col):
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
        if (self.get(row, col) == FieldValue.NONE):
            surroundingValues = [
                # row above desired field to fill
                self.getFieldValue(rowIdx - 1, colIdx - 1), self.getFieldValue(rowIdx - 1, colIdx), self.getFieldValue(rowIdx - 1, colIdx + 1),
                # row at desired field to fill
                self.getFieldValue(rowIdx, colIdx - 1),                                             self.getFieldValue(rowIdx, colIdx + 1),
                # row below desired field to fill
                self.getFieldValue(rowIdx + 1, colIdx - 1), self.getFieldValue(rowIdx + 1, colIdx), self.getFieldValue(rowIdx + 1, colIdx + 1)
            ]
            return any(x == FieldValue.WHITE or x == FieldValue.BLACK for x in surroundingValues)
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
            return FieldValue.NONE
        else:
            col = self.columns[colIdx]
            return self.get(rowIdx+1, col)

    
    def flipValues(self, row, col):
        """Flips the values after a legal move came through
        
        Arguments:
            row {int} -- Row of the move resulting in the flippin'
            col {str} -- Col of the move resulting in the flippin'

        Returns:
            Boolean -- True if flipped any values, False is not
        """
        playerValue = FieldValue.WHITE if self.turn == self.white else FieldValue.BLACK

        star = [
            self.getHorizontal_Left(row, col),
            self.getHorizontal_Right(row, col),
            self.getVertical_top(row, col),
            self.getVertical_bot(row, col),
            self.getDiagonal_topLeft(row, col),
            self.getDiagonal_topRight(row, col),
            self.getDiagonal_botLeft(row, col),
            self.getDiagonal_botRight(row, col),
        ]
        try:
            # flip values for move
            fieldsFlipped = 0
            for arr in star:
                fieldsFlipped+=self.flipFieldArray(arr)
            if (fieldsFlipped > 0):
                self.set(row, col, playerValue)
                self.turn = self.white if self.turn == self.black else self.black
            # flip turn value
            # flip playability values
            # for row in self.board.grid:
            #     for field in row:
            #         field.playableBy = CanBePlayedBy.NONE
            #         if self.checkBorderedToStone(field.row, field.col):
            #             canflip = [
            #                 self.canFlip(self.getHorizontal_Left(field.row, field.col)),
            #                 self.canFlip(self.getHorizontal_Right(field.row, field.col)),
            #                 self.canFlip(self.getVertical_top(field.row, field.col)),
            #                 self.canFlip(self.getVertical_bot(field.row, field.col)),
            #                 self.canFlip(self.getDiagonal_topLeft(field.row, field.col)),
            #                 self.canFlip(self.getDiagonal_topRight(field.row, field.col)),
            #                 self.canFlip(self.getDiagonal_botLeft(field.row, field.col)),
            #                 self.canFlip(self.getDiagonal_botRight(field.row, field.col)),
            #             ]
            #             if any(canflip):
            #                 playabalityValue = CanBePlayedBy.BLACK if self.playerValue == FieldValue.BLACK else CanBePlayedBy.WHITE
            #                 field.addPlayability(playabalityValue)
        except:
            pass

    def flipFieldArray(self, fields):
        """Flips the fields based on the reversi rules
        Returns True if at least one field was flipped
        
        Arguments:
            fields {Field[]} -- Array of fields to flip

        Returns:
            Boolean -- canflip
        """
        fieldsFlipped = 0
        if self.canFlip(fields):
            i = 0
            while (i < len(fields)) & (fields[i].playedBy != self.playerValue) & (fields[i].playedBy != 0):
                if fields[i].playedBy == self.opponentValue:
                    fields[i].playedBy = self.playerValue
                    fieldsFlipped+=1
                i+=1
        return fieldsFlipped
        

    def canFlip(self, fields):
        canFlip = False
        if len(fields) != 0:
            if fields[0].playedBy == self.opponentValue:
                for f in range(1, len(fields)):
                    if fields[f].playedBy == self.playerValue:
                        canFlip = True
                        break                
        return canFlip


    def createFieldArray(self, row, col, directionalCallback):
        f = self.board.get(row, col)
        currentField = directionalCallback(f)
        fields = []
        if currentField != None:
            if currentField.playedBy != 0:
                fields.append(currentField)
                while (directionalCallback(currentField) != None):
                    currentField = directionalCallback(currentField)
                    fields.append(currentField)
        
        return fields

    def getHorizontal_Left(self, row, col):
        """Flips stones left of the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col

        Returns:
            Field[] -- Array of fields to check and flip
        """
        return self.createFieldArray(row, col, self.board.left)

    def getHorizontal_Right(self, row, col):
        """Flips stones right of the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col

        Returns:
            Field[] -- Array of fields to check and flip
        """
        return self.createFieldArray(row, col, self.board.right)

    def getVertical_top(self, row, col):
        """Flips stones above the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col
            
        Returns:
            Field[] -- Array of fields to check and flip
        """
        return self.createFieldArray(row, col, self.board.top)

    def getVertical_bot(self, row, col):
        """Flips stones belowthe move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col

        Returns:
            Field[] -- Array of fields to check and flip
        """
        return self.createFieldArray(row, col, self.board.bottom)

    def getDiagonal_topLeft(self,row,col):
        """Flips stones top left of the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col

        Returns:
            Field[] -- Array of fields to check and flip
        """
        return self.createFieldArray(row, col, self.board.topLeft)
    
    def getDiagonal_topRight(self,row,col):
        """Flips stones top right of the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col

        Returns:
            Field[] -- Array of fields to check and flip
        """
        return self.createFieldArray(row, col, self.board.topRight)

    def getDiagonal_botLeft(self, row, col):
        """Flips stones bot left of the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col

        Returns:
            Field[] -- Array of fields to check and flip
        """
        return self.createFieldArray(row, col, self.board.botLeft)

    def getDiagonal_botRight(self,row,col):
        """Flips stones bot right of the move made
        !!! look out !!! have to know what you're doing !!!
        
        Arguments:
            row {int} -- Row
            col {str} -- col

        Returns:
            Field[] -- Array of fields to check and flip
        """
        return self.createFieldArray(row, col, self.board.botRight)