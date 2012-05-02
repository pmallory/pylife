import curses
import itertools
import time

# initial board configuration. A board's state is represented by the set
# of coordinates of living cells.
gen1 = set([(31, 32), (31, 33), (32, 31), (32, 32), (33, 32)])

def iterate(board, board_size):
    """Given a board state generate the next generation and return it.

    board: a set representing a genration's state
    board_size: how wide the (square) board is. Cells beyond this are
                effectively dead.

    """
    new_board = set()

    for cell in itertools.product(range(board_size), repeat=2):
        # count cell's neigbors
        neighbour_count = 0
        if (cell[0]-1, cell[1]-1) in board:
            neighbour_count += 1
        if (cell[0]-1, cell[1]) in board:
            neighbour_count += 1
        if (cell[0]-1, cell[1]+1) in board:
            neighbour_count += 1
        if (cell[0], cell[1]-1) in board:
            neighbour_count += 1
        if (cell[0], cell[1]+1) in board:
            neighbour_count += 1
        if (cell[0]+1, cell[1]-1) in board:
            neighbour_count += 1
        if (cell[0]+1, cell[1]) in board:
            neighbour_count += 1
        if (cell[0]+1, cell[1]+1) in board:
            neighbour_count += 1

        # determine which cells will be alive on the next generation
        if cell in board:
            if 2 <= neighbour_count <= 3:
                new_board.add(cell)
        elif neighbour_count is 3:
            new_board.add(cell)

    return new_board


def main(stdscr):
    current_gen = gen1

    # hide the cursor
    curses.curs_set(0)

    # set the board size such that it fits within the terminal window
    board_size = min(stdscr.getmaxyx())

    while True:
        # draw living cells
        for cell_coords in current_gen:
            stdscr.addch(cell_coords[0], cell_coords[1], 'O')
        stdscr.refresh()

        time.sleep(0.1)
        stdscr.erase()
        current_gen = iterate(current_gen, board_size)

if __name__=='__main__':
    curses.wrapper(main)

