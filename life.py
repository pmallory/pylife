import itertools
import os
import sys
import time

board_size = 60

gen1 = {(21,22):True, (21,23):True, (22,21):True, (22,22):True, (23,22):True}

def iterate(board):
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
            else:
                new_board[cell] = False
        elif neighbour_count is 3:
            new_board[cell] = True
        else:
            new_board[cell] = False

    return new_board

current_gen = gen1
clear_console = 'clear' if os.name == 'posix' else 'CLS'

while True:
    out = ''
    for (i, cell) in enumerate(itertools.product(range(board_size), repeat=2)):
        if current_gen.get(cell):
            out += 'X'
        else:
            out += ' '
        if (i+1)%board_size==0:
            out += '\n'

    os.system(clear_console)
    sys.stdout.write(out)
    sys.stdout.flush()
    time.sleep(0.1)
    current_gen = iterate(current_gen)