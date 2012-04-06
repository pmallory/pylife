import curses
import itertools
import os
import sys
import time

gen1 = {(31,32):True, (31,33):True, (32,31):True, (32,32):True, (33,32):True}

board_size = 60

def iterate(board, board_size):
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
    curses.curs_set(0)

    board_size = min(stdscr.getmaxyx())

    while True:
        for (i, cell_coords) in enumerate(itertools.product(range(board_size), repeat=2)):
            if current_gen.get(cell_coords):
                stdscr.addch(cell_coords[0], cell_coords[1], 'X')
        stdscr.refresh()

        time.sleep(0.1)
        stdscr.erase()
        current_gen = iterate(current_gen, board_size)

if __name__=='__main__':
    curses.wrapper(main)

