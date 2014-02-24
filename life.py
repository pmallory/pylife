import curses
from itertools import product, ifilter, islice, cycle
import random
import time

# cycling iterator of a cell's eight neigbors
neighbors = cycle(ifilter(lambda x: x!=(0,0), product(xrange(-1,2), repeat=2)))

def iterate(board, board_size):
    """Given a board state generate the next generation and return it.

    board: a set of tuples representing living cells.
    board_size: The dimesnions of the world. Cells beyond this are
                effectively dead.
    """
    new_board = set()

    for cell in product(xrange(board_size[0]), xrange(board_size[1])):
        # count cell's living neighbors
        neighbor_count = 0
        for neighbor in islice(neighbors, 8):
            if (cell[0]+neighbor[0], cell[1]+neighbor[1]) in board:
                neighbor_count += 1

        # determine which cells will be alive on the next generation
        if cell in board:
            if 2 <= neighbor_count <= 3:
                new_board.add(cell)
        elif neighbor_count is 3:
            new_board.add(cell)

    return new_board

def main(stdscr):
    # a generation is a set of living cells
    current_gen = set()

    # randomize the first generation
    board_size = stdscr.getmaxyx()
    for cell in product(xrange(board_size[0]), xrange(board_size[1])):
        # 1/5 chance of cell being alive
        if random.choice([True] + 4*[False]):
            current_gen.add(cell)

    # make getch() non-blocking
    stdscr.nodelay(1)

    # hide the cursor
    curses.curs_set(0)

    while True:
        # set the board size such that it fits within the terminal window
        board_size = stdscr.getmaxyx()

        # generate the next time step from the current
        current_gen = iterate(current_gen, board_size)

        # erase the screen
        stdscr.erase()

        # draw the new generation of cells
        for cell_coords in current_gen:
            stdscr.addch(cell_coords[0], cell_coords[1], 'O')
        stdscr.refresh()

        # exit if user presses q
        if stdscr.getch() == ord('q'):
            break

        # slow the animation
        time.sleep(0.1)

if __name__=='__main__':
    curses.wrapper(main)

