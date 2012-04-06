import curses
import itertools
import os
import sys
import time

# initial board configuration. The board is a dictionary mapping
# cell coords=>cell state. Dead cells can have a value of False, or they can
# can be left out entirely
gen1 = {(31,32):True, (31,33):True, (32,31):True, (32,32):True, (33,32):True}

def iterate(board, board_size):
    """Given a board state generate the next generation and return it.

    board: a dictionary representing a genration's state
    board_size: how wide the (square) board is. Cells beyond this are
                effectively dead.

    """
    new_board = {}

    for cell in itertools.product(range(board_size), repeat=2):
        # count cell's neigbors
        neighbour_count = 0
        if board.get((cell[0]-1, cell[1]-1)):
            neighbour_count += 1
        if board.get((cell[0]-1, cell[1])):
            neighbour_count += 1
        if board.get((cell[0]-1, cell[1]+1)):
            neighbour_count += 1
        if board.get((cell[0], cell[1]-1)):
            neighbour_count += 1
        if board.get((cell[0], cell[1]+1)):
            neighbour_count += 1
        if board.get((cell[0]+1, cell[1]-1)):
            neighbour_count += 1
        if board.get((cell[0]+1, cell[1])):
            neighbour_count += 1
        if board.get((cell[0]+1, cell[1]+1)):
            neighbour_count += 1

        # determine which cells will be alive on the next generation
        if board.get(cell):
            if 2 <= neighbour_count <= 3:
                new_board[cell] = True
        elif neighbour_count is 3:
            new_board[cell] = True

    return new_board


def main(stdscr):
    current_gen = gen1

    # hide the cursor
    curses.curs_set(0)

    # set the board size such that it fits within the terminal window
    board_size = min(stdscr.getmaxyx())

    while True:
        # draw living cells
        # TODO this can by way more efficient.
        for cell_coords in itertools.product(range(board_size), repeat=2):
            if current_gen.get(cell_coords):
                stdscr.addch(cell_coords[0], cell_coords[1], 'X')
        stdscr.refresh()

        time.sleep(0.1)
        stdscr.erase()
        current_gen = iterate(current_gen, board_size)

if __name__=='__main__':
    curses.wrapper(main)

