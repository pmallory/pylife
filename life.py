import time
import os
import sys

gen1 = {(0,0): False, (0,1):False, (0,2):False,
        (1,0): True,  (1,1):True,  (1,2):True,
        (2,0): False, (2,1):False, (2,2):False }

def iterate(board):
    new_board = {}

    for cell in board:
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

def print_board(board):
    for cell in board:
        if board[cell]:
            print str(cell) + str(board[cell])



current_gen = gen1
clear_console = 'clear' if os.name == 'posix' else 'CLS'

while True:
    out = ''
    for (i, cell) in enumerate(sorted(current_gen)):
        if current_gen[cell]:
            out += 'X'
        else:
            out += ' '
        if (i+1)%3==0:
            out += '\n'
