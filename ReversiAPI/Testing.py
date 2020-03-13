from Reversi import Game
from Board import Field, Grid

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
    assert game.legalMove(1, 'A') == False

def test_legalMoveShouldSucceed():
    game = newGame()
    assert game.legalMove(3, "C")


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
    grid.set(4, 'd', -1)
    valueGrid = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, -1,-1, 0, 0, 0],
                [0, 0, 0,-1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    assert valueGrid == grid.toFieldValueArray()

def test_GettingField():
    grid = Grid(columns)
    assert grid.get(4, 'd').playedBy == 1
    assert grid.get(4, 'e' ).playedBy == -1

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
    assert game.board.toFieldValueArray() == valueGrid

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
    assert (game.board.toFieldValueArray() == valueGrid) == False

def test_flipHorizontalLeft():
    game = newGame()
    game.flipHorizontal_Left(5, 'f')
    valueGrid = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1,-1, 0, 0, 0],
                [0, 0, 0,-1, -1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    assert (game.board.toFieldValueArray() == valueGrid)

def test_flipHorizontalRight():
    game = newGame()
    game.flipHorizontal_Right(4, 'c')
    valueGrid = [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, -1,-1, 0, 0, 0],
                [0, 0, 0,-1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    assert (game.board.toFieldValueArray() == valueGrid)

def test_flipVerticalTop():
    game = newGame()
    game.flipVertical_top(6, 'e')
    valueGrid =[
        #        a  b  c  d  e  f  g  h    
                [0, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 0, 0, 0, 0, 0, 0], # 2
                [0, 0, 0, 0, 0, 0, 0, 0], # 3
                [0, 0, 0, 1,-1, 0, 0, 0], # 4
                [0, 0, 0,-1,-1, 0, 0, 0], # 5
                [0, 0, 0, 0, 0, 0, 0, 0], # 6
                [0, 0, 0, 0, 0, 0, 0, 0], # 7
                [0, 0, 0, 0, 0, 0, 0, 0]] # 8
    assert (game.board.toFieldValueArray() == valueGrid)

def test_flipVerticalBot():
    game = newGame()
    game.flipVertical_bot(3, 'd')
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
    assert (game.board.toFieldValueArray() == valueGrid)

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
    game.flipDiagonal_topLeft(6, 'f')
    assert (game.board.toFieldValueArray() == newValueGrid)


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
    game.flipDiagonal_topRight(6, 'c')
    assert (game.board.toFieldValueArray() == newValueGrid)

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

    game.flipDiagonal_botLeft(3, 'f')
    assert (game.board.toFieldValueArray() == newValueGrid)

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

    game.flipDiagonal_botRight(3, 'c')
    assert (game.board.toFieldValueArray() == newValueGrid)