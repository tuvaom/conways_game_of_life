import numpy as np
from life_game import *


def test_check_neighbours():
    #zero is zero
    a = np.array([[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]])
    assert check_neighbours(1, 1, a) == 0

    # skip center
    a = np.array([[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]])
    assert check_neighbours(1, 1, a) == 0

    # count top
    a = np.array([[1, 1, 1],
                  [0, 0, 0],
                  [0, 0, 0]])
    assert check_neighbours(1, 1, a) == 3

    # count bottom
    a = np.array([[0, 0, 0],
                  [0, 0, 0],
                  [1, 1, 1]])
    assert check_neighbours(1, 1, a) == 3

    # count left
    a = np.array([[1, 0, 0],
                  [1, 0, 0],
                  [1, 0, 0]])
    assert check_neighbours(1, 1, a) == 3

    # count specific
    a = np.array([[1, 0, 0],
                  [0, 0, 1],
                  [1, 0, 0]])
    assert check_neighbours(1, 1, a) == 3

    # count all around
    a = np.array([[1, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])
    assert check_neighbours(1, 1, a) == 8

    # all alive
    a = np.array([[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]])
    assert check_neighbours(1, 1, a) == 8


def test_init_board():
    board = init_board(10, 10)
    assert board.shape[0] == 10 and board.shape[1] == 10

    board = init_board(100, 10)
    assert board.shape[0] == 100 and board.shape[1] == 10

    board = init_board(10, 100)
    assert board.shape[0] == 10 and board.shape[1] == 100


def test_get_next_board():
    a = np.array([[0, 0, 0, 0],
                  [1, 1, 1, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]])

    b = np.array([[0, 1, 0, 0],
                  [0, 1, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0]])
    assert np.array_equal(get_next_board(a), b)

    a = np.array([[0, 0, 0, 0],
                  [0, 1, 1, 0],
                  [0, 1, 1, 0],
                  [0, 0, 0, 0]])

    b = np.array([[0, 0, 0, 0],
                  [0, 1, 1, 0],
                  [0, 1, 1, 0],
                  [0, 0, 0, 0]])
    assert np.array_equal(get_next_board(a), b)


def test_read_board():
    board = read_board("square.board")
    true_board = np.array([[0, 0, 0, 0],
                           [0, 1, 1, 0],
                           [0, 1, 1, 0],
                           [0, 0, 0, 0]])
    np.array_equal(board, true_board)
