from Reversi import Game
from Board import Field, Grid, FieldValue

import pytest

columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def CreateEmptyGrid():
    return {   #idx:  0, 1, 2, 3, 4, 5, 5, 7 
               #row:  1, 2, 3, 4, 5, 6, 7, 8   
                "A": [0, 0, 0, 0, 0, 0, 0, 0],
                "B": [0, 0, 0, 0, 0, 0, 0, 0],
                "C": [0, 0, 0, 0, 0, 0, 0, 0],
                "D": [0, 0, 0, 1,-1, 0, 0, 0],
                "E": [0, 0, 0,-1, 1, 0, 0, 0],
                "F": [0, 0, 0, 0, 0, 0, 0, 0],
                "G": [0, 0, 0, 0, 0, 0, 0, 0],
                "H": [0, 0, 0, 0, 0, 0, 0, 0],
            }   

def newGame():
    return Game('gameToken', 'black', 'white')


def test_legalMoveTopLeftShouldFail():
    game = newGame()
    assert game.checkBorderedToStone(1, 'A') == False

def test_legalMoveShouldSucceed():
    game = newGame()
    assert game.checkBorderedToStone(3, "C")


def test_GridColumnsShouldBeLowerCased():
    grid = Grid(columns)
    assert all(col.islower() for col in grid.columns)


def test_GridConstructor():
    gridStr = str(
        [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1,-1, 0, 0, 0],
        [0, 0, 0,-1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]
    )
    grid = Grid(columns)
    assert gridStr == str(grid)

def test_SettingField():
    grid = Grid(columns)
    grid.set(4, 'd', FieldValue.BLACK)
    valueGrid = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, -1,-1, 0, 0, 0],
                [0, 0, 0,-1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    assert valueGrid == grid.valueGrid

def test_GettingField():
    grid = Grid(columns)
    assert grid.get(4, 'd').playedBy == FieldValue.WHITE
    assert grid.get(4, 'e' ).playedBy == FieldValue.BLACK

def test_gameUpdateChosenFieldShouldBeBlack():
    game = newGame()
    game.update('black', 6, 'e')
    valueGrid = [
        #        a  b  c  d  e  f  g  h    
                [0, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 0, 0, 0, 0, 0, 0], # 2
                [0, 0, 0, 0, 0, 0, 0, 0], # 3
                [0, 0, 0, 1,-1, 0, 0, 0], # 4
                [0, 0, 0,-1,-1, 0, 0, 0], # 5
                [0, 0, 0, 0,-1, 0, 0, 0], # 6
                [0, 0, 0, 0, 0, 0, 0, 0], # 7
                [0, 0, 0, 0, 0, 0, 0, 0]] # 8
    assert game.board.valueGrid == valueGrid

def test_gameUpdateChosenFieldShouldBeBlack_ShouldFail():
    game = newGame()
    game.update('black', 6, 'e')
    valueGrid = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1,-1, 0, 0, 0],
                [0, 0, 0,-1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    assert (game.board.valueGrid == valueGrid) == False

def test_flipHorizontalLeft():
    game = newGame()
    left = game.getHorizontal_Left(5, 'f')
    game.flipFieldArray(left)
    valueGrid = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1,-1, 0, 0, 0],
                [0, 0, 0,-1, -1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    assert (game.board.valueGrid == valueGrid)

def test_flipHorizontalRight():
    game = newGame()
    right = game.getHorizontal_Right(4, 'c')
    game.flipFieldArray(right)
    valueGrid = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, -1,-1, 0, 0, 0],
                [0, 0, 0,-1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    assert (game.board.valueGrid == valueGrid)

def test_flipVerticalTop():
    game = newGame()
    top = game.getVertical_top(6, 'e')
    game.flipFieldArray(top)
    valueGrid = [
        #        a  b  c  d  e  f  g  h    
                [0, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 0, 0, 0, 0, 0, 0], # 2
                [0, 0, 0, 0, 0, 0, 0, 0], # 3
                [0, 0, 0, 1,-1, 0, 0, 0], # 4
                [0, 0, 0,-1,-1, 0, 0, 0], # 5
                [0, 0, 0, 0, 0, 0, 0, 0], # 6
                [0, 0, 0, 0, 0, 0, 0, 0], # 7
                [0, 0, 0, 0, 0, 0, 0, 0]] # 8
    assert (game.board.valueGrid == valueGrid)

def test_flipVerticalBot():
    game = newGame()
    bot = game.getVertical_bot(3, 'd')
    game.flipFieldArray(bot)
    valueGrid =[
        #        a  b  c  d  e  f  g  h    
                [0, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 0, 0, 0, 0, 0, 0], # 2
                [0, 0, 0, 0, 0, 0, 0, 0], # 3
                [0, 0, 0,-1,-1, 0, 0, 0], # 4
                [0, 0, 0,-1, 1, 0, 0, 0], # 5
                [0, 0, 0, 0, 0, 0, 0, 0], # 6
                [0, 0, 0, 0, 0, 0, 0, 0], # 7
                [0, 0, 0, 0, 0, 0, 0, 0]] # 8
    assert (game.board.valueGrid == valueGrid)

def test_flipDiagionalTopLeft():
    game = newGame()
    game.addGrid(
        [
        #        a  b  c  d  e  f  g  h    
                [0, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 0, 0, 0, 0, 0, 0], # 2
                [0, 0,-1, 0, 0, 0, 0, 0], # 3
                [0, 0, 0, 1,-1, 0, 0, 0], # 4
                [0, 0, 0,-1, 1, 0, 0, 0], # 5
                [0, 0, 0, 0, 0, 0, 0, 0], # 6
                [0, 0, 0, 0, 0, 0, 0, 0], # 7
                [0, 0, 0, 0, 0, 0, 0, 0]] # 8
    )
    newValueGrid = [
        #        a  b  c  d  e  f  g  h    
                [0, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 0, 0, 0, 0, 0, 0], # 2
                [0, 0,-1, 0, 0, 0, 0, 0], # 3
                [0, 0, 0,-1,-1, 0, 0, 0], # 4
                [0, 0, 0,-1,-1, 0, 0, 0], # 5
                [0, 0, 0, 0, 0, 0, 0, 0], # 6
                [0, 0, 0, 0, 0, 0, 0, 0], # 7
                [0, 0, 0, 0, 0, 0, 0, 0]] # 8
    topleft =  game.getDiagonal_topLeft(6, 'f')
    game.flipFieldArray(topleft)
    assert (game.board.valueGrid == newValueGrid)


def test_flipDiagionalTopRight():
    game = newGame()
    game.addGrid(
        [
        #        a  b  c  d  e  f  g  h    
                [0, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 0, 0, 0, 0, 0, 0], # 2
                [0, 0, 0, 0, 0, -1, 0, 0], # 3
                [0, 0, 0,-1, 1, 0, 0, 0], # 4
                [0, 0, 0, 1,-1, 0, 0, 0], # 5
                [0, 0, 0, 0, 0, 0, 0, 0], # 6
                [0, 0, 0, 0, 0, 0, 0, 0], # 7
                [0, 0, 0, 0, 0, 0, 0, 0]] # 8
    )
    newValueGrid = [
        #        a  b  c  d  e  f  g  h    
                [0, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 0, 0, 0, 0, 0, 0], # 2
                [0, 0, 0, 0, 0,-1, 0, 0], # 3
                [0, 0, 0, -1,-1, 0, 0, 0], # 4
                [0, 0, 0,-1, -1, 0, 0, 0], # 5
                [0, 0, 0, 0, 0, 0, 0, 0], # 6
                [0, 0, 0, 0, 0, 0, 0, 0], # 7
                [0, 0, 0, 0, 0, 0, 0, 0]] # 8
    topright = game.getDiagonal_topRight(6, 'c')
    game.flipFieldArray(topright)
    assert (game.board.valueGrid == newValueGrid)

def test_flipDiagionalBotLeft():
    game = newGame()
    game.addGrid([
        #        a  b  c  d  e  f  g  h    
                [0, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 0, 0, 0, 0, 0, 0], # 2
                [0, 0, 0, 0, 0, 0, 0, 0], # 3
                [0, 0, 0,-1, 1, 0, 0, 0], # 4
                [0, 0, 0, 1,-1, 0, 0, 0], # 5
                [0, 0,-1, 0, 0, 0, 0, 0], # 6
                [0, 0, 0, 0, 0, 0, 0, 0], # 7
                [0, 0, 0, 0, 0, 0, 0, 0]] # 8
    )
    newValueGrid = [
        #        a  b  c  d  e  f  g  h    
                [0, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 0, 0, 0, 0, 0, 0], # 2
                [0, 0, 0, 0, 0, 0, 0, 0], # 3
                [0, 0, 0,-1,-1, 0, 0, 0], # 4
                [0, 0, 0,-1,-1, 0, 0, 0], # 5
                [0, 0,-1, 0, 0, 0, 0, 0], # 6
                [0, 0, 0, 0, 0, 0, 0, 0], # 7
                [0, 0, 0, 0, 0, 0, 0, 0]] # 8

    botleft = game.getDiagonal_botLeft(3, 'f')
    game.flipFieldArray(botleft)
    assert (game.board.valueGrid == newValueGrid)

def test_flipDiagionalBotRight():
    game = newGame()
    game.addGrid([
        #        a  b  c  d  e  f  g  h    
                [0, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 0, 0, 0, 0, 0, 0], # 2
                [0, 0, 0, 0, 0, 0, 0, 0], # 3
                [0, 0, 0, 1,-1, 0, 0, 0], # 4
                [0, 0, 0,-1, 1, 0, 0, 0], # 5
                [0, 0, 0, 0, 0,-1, 0, 0], # 6
                [0, 0, 0, 0, 0, 0, 0, 0], # 7
                [0, 0, 0, 0, 0, 0, 0, 0]] # 8
    )
    newValueGrid = [
        #        a  b  c  d  e  f  g  h    
                [0, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 0, 0, 0, 0, 0, 0], # 2
                [0, 0, 0, 0, 0, 0, 0, 0], # 3
                [0, 0, 0,-1,-1, 0, 0, 0], # 4
                [0, 0, 0,-1,-1, 0, 0, 0], # 5
                [0, 0, 0, 0, 0,-1, 0, 0], # 6
                [0, 0, 0, 0, 0, 0, 0, 0], # 7
                [0, 0, 0, 0, 0, 0, 0, 0]] # 8

    botright = game.getDiagonal_botRight(3, 'c')
    game.flipFieldArray(botright)
    assert (game.board.valueGrid == newValueGrid)