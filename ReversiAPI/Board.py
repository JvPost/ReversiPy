class Grid:
    def __init__(self, collumnArray):
        self.columns = [col.lower() for col in collumnArray]
        self.grid = []
        row = 1
        for column in self.columns:
            self.grid.append([])
            for column in self.columns:
                self.grid[row-1].append(Field(row, column, FieldValue.NONE))
            row+=1
        self.set(4, 'd', FieldValue.WHITE)
        self.set(4, 'e', FieldValue.BLACK)
        self.set(5, 'd', FieldValue.BLACK)
        self.set(5, 'e', FieldValue.WHITE)

        # # can be played by black
        # self.get(6, 'e').canBePlayedBy = CanBePlayedBy.BLACK.value
        # self.get(5, 'f').canBePlayedBy = CanBePlayedBy.BLACK.value
        # self.get(4, 'c').canBePlayedBy = CanBePlayedBy.BLACK.value
        # self.get(3, 'd').canBePlayedBy = CanBePlayedBy.BLACK.value

    def __str__(self):
        valueGrid = self.valueGrid
        intValueGrid = []
        for row in valueGrid:
            valueRow = []
            for field in row:
                valueRow.append(field)
            intValueGrid.append(valueRow)
            
        return str(intValueGrid)

    @property
    def valueGrid(self):
        valueGrid = []
        i = 0
        for row in self.grid:
            valueGrid.append([])
            for field in row:
                valueGrid[i].append(field.playedBy.value)
            i+=1
        return valueGrid
    
    def columnIndex(self, column):
        """Returns index of a column
        
        Arguments:
            column {str} -- str of column
        
        Returns:
            int -- index of column in columnarray
        """
        if (column in self.columns):
            return self.columns.index(column)
        else:
            return -1

    def set(self, row, col, value):
        """Sets a playedBy value of field on row and col on grid
        
        Arguments:
            row {int} -- Row in game field. Index of row in grid is row minus one.
            col {str} -- Column in game field.
            value {FieldValue} -- Value of field, 1 for white, -1 for black, 0 for neither
        """
        self.grid[row - 1][self.columns.index(col.lower())].playedBy = value


    def get(self, row, col):
        """Returns a field of game grid. If index out of range returns 0
        
        Arguments:
            row {int} -- Row in game field. Index of row in grid is row minus one.
            col {str} -- Column in game field.
        
        Returns:
            Field -- Field object
        """
        try:
            field = self.grid[row - 1][self.columns.index(col.lower())]
            return field
        except IndexError:
            return 0
        else:
            raise("Couldn't get value from grid")

    def topLeft(self, field):
        """Returns the topleft of the field parameter,
        returns None is top left doesn't exist
        
        Arguments:
            field {Field} -- Field

        Returns:
            Field -- Top left field            
        """
        f = None
        if (field.row != 1) & (field.col != self.columns[0]):
            f =  self.get(field.row - 1, self.columns[self.columnIndex(field.col) - 1])
        return f

    def top(self, field):
        f = None
        if field.row != 1:
            f = self.get(field.row - 1, self.columns[self.columnIndex(field.col)])
        return f

    def topRight(self, field):
        f = None
        if (field.row != 1) & (self.columns[-1] != field.col):
            f = self.get(field.row - 1, self.columns[self.columnIndex(field.col) + 1])
        return f

    def left(self, field):
        f = None
        if (field.col != self.columns[0]):
            f = self.get(field.row, self.columns[self.columnIndex(field.col) - 1])
        return f

    def right(self, field):
        f = None
        if (field.col != self.columns[-1]):
            f = self.get(field.row, self.columns[self.columnIndex(field.col) + 1])
        return f

    def botLeft(self, field):
        f = None
        if (field.row != len(self.columns)) & (field.col != self.columns[0]):
            f = self.get(field.row + 1, self.columns[self.columnIndex(field.col) - 1])
        return f
    
    def bottom(self, field):
        f = None
        if (field.row != len(self.columns)):
            f = self.get(field.row + 1, self.columns[self.columnIndex(field.col)])
        return f

    def botRight(self, field):
        f = None
        if (field.row != len(self.columns)) & (field.col != self.columns[-1]):
            f = self.get(field.row + 1, self.columns[self.columnIndex(field.col) + 1])
        return f

class Field:
    def __init__(self, row, col, playedBy):
        """
        Represents a field in the Reversi game field
        
        Arguments:
            col {string} -- Column of field in grid (for name)
            row {int} -- Row of field in grid (for name)
            playedBy {FieldValue} -- Which player played the field, -1 for black, 1 for white, 0 for neither 
        """
        self.col = col
        self.row = row
        self.playedBy = FieldValue.NONE
        self.playableBy = CanBePlayedBy.NONE

    def __int__(self):
        """Returns playedBy field
        
        Returns:
            int -- value of PlayedByField
        """
        return self.playedBy


    def addPlayability(self, canBePlayedBy):
        """ Changes the canBePlayedBy value to black white or both, based on current canBePlayed parameter value and canBePlayed instance variable value
        
        Arguments:
            canBePlayedBy {CanBePlayedBy} -- [description]
        """

        if canBePlayedBy == CanBePlayedBy.NONE:
            raise("Can't add CanBePlayedBy.NONE as a player to field" )

        if self.playableBy != canBePlayedBy and self.playableBy != CanBePlayedBy.NONE:
            self.playableBy = CanBePlayedBy.BOTH
        elif self.playableBy == CanBePlayedBy.BOTH | self.playableBy == canBePlayedBy:
            pass
        else:
            self.playableBy = canBePlayedBy

    def removePlayability(self, canBePlayedBy):
        """Removes a player from the canBePlayedBy instance variable 
        
        Arguments:
            canBePlayedBy {[type]} -- [description]
        """
        if canBePlayedBy == CanBePlayedBy.NONE:
            raise("Can't remove CanBePlayedBy.NONE as a player to field" )

        if self.playableBy == CanBePlayedBy.BOTH:
            if (canBePlayedBy == CanBePlayedBy.WHITE):
                self.playableBy = CanBePlayedBy.BLACK
            elif (canBePlayedBy == CanBePlayedBy.BLACK):
                self.playableBy = CanBePlayedBy.WHITE
            elif (canBePlayedBy == CanBePlayedBy.BOTH):
                self.playableBy = CanBePlayedBy.NONE
        elif canBePlayedBy == self.playableBy:
            self.playableBy = CanBePlayedBy.NONE


from enum import Enum
class FieldValue(Enum):
    BLACK = -1
    WHITE = 1
    NONE = 0

    def __str__(self):
        return str(self.value)
    
class CanBePlayedBy(Enum):
    BLACK = -1
    WHITE = 1
    NONE = 0
    BOTH = 2

    def __str__(self):
        return str(self.value)