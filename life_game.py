import numpy as np


def check_neighbours(r, c, board):
    NeighboursSum = 0

    for x in range(r - 1, r + 2):
        for y in range(c - 1, c + 2):
            if x == r and c == y:
                continue
            else:
                NeighboursSum = NeighboursSum + board[x][y]

    return NeighboursSum


def init_board(rows, columns, method="random", filepath=""):
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
    return np.pad(board, (1,), 'wrap')


def get_next_board(paddedBoard):
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
