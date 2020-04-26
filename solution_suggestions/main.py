import matplotlib.pyplot as plt
import life_game as lg
import os

def main():
    if not os.path.exists('results'):
        os.makedirs('results')

    rows = 40
    columns = 40
    iterations = 100
    sizeup = 10

    board = lg.init_board(rows, columns)
    # board = lg.init_board(rows,
    #                       columns,
    #                       method="read",
    #                       filepath="boards/hwss.board")

    for it in range(iterations):
        nextBoard = lg.get_next_board(board)

        biggerBoard = nextBoard.repeat(sizeup, axis=0)
        biggerBoard = biggerBoard.repeat(sizeup, axis=1)

        plt.imshow(biggerBoard,'gray')
        plt.savefig(str("results/test%d.png" % it), bbox_inches='tight')

        board = nextBoard
        print("iteration ", it+1,"/",iterations)

main()
