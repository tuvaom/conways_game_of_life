"""life_game module.

This module has all the functions needed to paly Conway's game of life


Example:
    The module can be imported as follows
        >>> import life_game as lg

Attributes:
    No attributes

Todo:
    * Incremental improvements

"""

import numpy as np


def check_neighbours(r, c, board):
    """sum neighbours of board element for Conway's game of life

    Extended description of function.

    Args:
        r (int): number of rows in board
        c (int): number of columns in board
        board (np.array): method for board initalization

    Returns:
        (int): sum of neighbour values for Conway's game of life

    Raises:
        None

    Examples:
        None
    """
    NeighboursSum = 0

    for x in range(r - 1, r + 2):
        for y in range(c - 1, c + 2):
            if (x ==r and y  == c):
                continue
             NeighboursSum += board[x][y]
    return NeighboursSum


def init_board(rows, columns, method="random"):
    """Initialize a board for Conway's game of life

    Extended description of function.

    Args:
        rows (int): number of rows in board
        columns (int): number of columns in board
        method (str): method for board initalization
            "random" : Initialize board radnomly

    Returns:
        np.array: a numpy matrix with dimensions of the loaded board

    Raises:
        None

    Examples:
        None
    """
    if method == "random":
        board = np.random.random_integers(2, size=(rows, columns)) - 1
    return board


def pad_board(board):
    """Gives a padding to a board in Conway's game of life

    Extended description of function.

    Args:
        board (np.array): a numpy matrix with dimensions of the original board

    Returns:
        np.array: a numpy matrix with dimensions +1 in all directions of the original board

    Raises:
        None

    Examples:
        None
    """
    board = np.pad(board, 1 , mode ='constant')

    return board


def get_next_board(Board):
    """Iterates from a paddedboard to the next board in Conway's game of life

    Extended description of function.

    Args:
        paddedBoard (np.array ): a numpy matrix with dimensions of
                                 the original board

    Returns:
        Board: a numpy matrix with dimensions of the original board
               updated to the next generation.

    Raises:
        None

    Examples:
        None
    """
    
    paddedBoard = pad_board(Board)

    dims = paddedBoard.shape
    rows = dims[0] - 2
    cols = dims[1] - 2

    
    nextBoard = np.zeros((rows, cols), dtype=int)

    for r in range(1, dims[0] - 1):
        for c in range(1, dims[1] - 1):
            numNeighbours = check_neighbours(r, c, paddedBoard) 
            #Game logic: 
            if paddedBoard[r][c] == 1:
                if (numNeighbours == 2 or numNeighbours ==3):
                    nextBoard[r-1][c-1] = 1

            else:
                if numNeighbours == 3:
                    nextBoard[r-1][c-1] = 1
            
    return nextBoard
