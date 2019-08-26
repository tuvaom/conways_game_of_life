from scipy.misc import toimage
import life_game as lg

def main():
    rows = 40
    columns = 40
    iterations = 100
    sizeup = 10

    board = lg.init_board(rows, columns)
    #board = lg.init_board(rows, columns, method="read", filepath="boards/aBoard.board")
    paddedBoard = lg.pad_board(board)

    for it in range(iterations):
        nextBoard = lg.get_next_board(paddedBoard)
        paddedBoard = lg.pad_board(nextBoard)

        biggerBoard = nextBoard.repeat(sizeup, axis=0)
        biggerBoard = biggerBoard.repeat(sizeup, axis=1)

        #im = Image.fromarray(biggerBoard,'1')
        im = toimage(biggerBoard)
        im.save(str("results/test%d.png" % it))


main()
