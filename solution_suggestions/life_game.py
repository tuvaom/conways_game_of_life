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
            if x == r and c == y:
                continue
            else:
                NeighboursSum = NeighboursSum + board[x][y]

    return NeighboursSum


def init_board(rows, columns, method="random", filepath=""):
    """Initialize a board for Conway's game of life

    Extended description of function.

    Args:
        rows (int): number of rows in board
        columns (int): number of columns in board
        method (str): method for board initalization
            "random" : Initialize board radnomly
            "one_glider": Initialize board with blinker
            "blinker": Initialize board with blinker
            "read": Load board from file, need filepath
        filepath (str): filepath to load board from file

    Returns:
        np.array: a numpy matrix with dimensions of the loaded board

    Raises:
        None

    Examples:
        None
    """

    if method == "random":
        board = np.random.random_integers(2, size=(rows, columns)) - 1
    elif method == "one_glider":
        board = np.zeros((rows, columns))
        if rows >= 3 and columns >= 3:
            board[0][1] = 1
            board[1][2] = 1
            board[2][0] = 1
            board[2][1] = 1
            board[2][2] = 1
    elif method == "blinker":
        board = np.zeros((rows, columns))
        if rows >= 3 and columns >= 3:
            board[1][0] = 1
            board[1][1] = 1
            board[1][2] = 1
    elif method == "read":
        board = read_board(filepath)
    return board


def read_board(filepath):
    """Load board from file in Conway's game of life

    Extended description of function.

    Args:
        filepath (str): The absolute or relative path of the board file

    Returns:
        np.array: a numpy matrix with dimensions of the loaded board

    Raises:
        None

    Examples:
        None
    """

    first = True
    if filepath == "":
        raise Exception("No board file specified")
    else:
        with open(filepath) as board_file:
            for line in board_file:
                li = list(line)
                arr = li[:-1]
                if first:
                    first = False
                    board = np.array([arr], dtype=int)
                else:
                    t = np.array(arr, dtype=int)
                    board = np.append(board, [t], axis=0)
    return board


def pad_board(board):
    """Gives a wrap padding to a board in Conway's game of life

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
    return np.pad(board, (1,), 'wrap')


def get_next_board(paddedBoard):
    """Iterates from a paddedboard to the next board in Conway's game of life

    Extended description of function.

    Args:
        paddedBoard (np.array ): a numpy matrix with dimensions +1
                                 in all directions of the original board

    Returns:
        nextBoard: a numpy matrix with dimensions  of the original board

    Raises:
        None

    Examples:
        None
    """
    dims = paddedBoard.shape
    rows = dims[0] - 2
    cols = dims[1] - 2

    nextBoard = np.zeros((rows, cols), dtype=int)

    for r in range(1, dims[0] - 1):
        for c in range(1, dims[1] - 1):
            numNeighbours = check_neighbours(r, c, paddedBoard)

            if paddedBoard[r][c] == 1:
                if numNeighbours < 2:
                    nextBoard[r - 1][c - 1] = 0
                elif numNeighbours == 2 or numNeighbours == 3:
                    nextBoard[r - 1][c - 1] = 1
                else:
                    nextBoard[r - 1][c - 1] = 0

            else:
                if numNeighbours == 3:
                    nextBoard[r - 1][c - 1] = 1
                else:
                    nextBoard[r - 1][c - 1] = 0

    return nextBoard
    