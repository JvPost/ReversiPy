class Field:
    def __init__(self, row, col, playedBy):
        """
        Represents a field in the Reversi game field
        
        Arguments:
            col {string} -- Column of field in grid (for name)
            row {int} -- Row of field in grid (for name)
            playedBy {int} -- Which player played the field, -1 for black, 1 for white, 0 for neither 
        """
        self.col = col
        self.row = row
        self.playedBy = playedBy

    def __int__(self):
        """Returns playedBy field
        
        Returns:
            int -- value of PlayedByField
        """
        return self.playedBy

class Grid:
    def __init__(self, collumnArray):
        self.columns = [col.lower() for col in collumnArray]
        self.grid = []
        row = 1
        for column in self.columns:
            self.grid.append([])
            for column in self.columns:
                self.grid[row-1].append(Field(row, column, 0))
            row+=1
        self.set(4, 'd', 1)
        self.set(4, 'e', -1)
        self.set(5, 'd', -1)
        self.set(5, 'e', 1)
        
    
    def __str__(self):
        valueGrid = self.toFieldValueArray()
        return str(valueGrid)

    def toFieldValueArray(self):
        valueGrid = []
        i = 0
        for row in self.grid:
            valueGrid.append([])
            for field in row:
                valueGrid[i].append(field.playedBy)
                
            i+=1
        return valueGrid

    def set(self, row, col, value):
        """Sets a playedBy value of field on row and col on grid
        
        Arguments:
            row {int} -- Row in game field. Index of row in grid is row minus one.
            col {str} -- Column in game field.
            value {int} -- Value of field, 1 for white, -1 for black, 0 for neither
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
    
    
