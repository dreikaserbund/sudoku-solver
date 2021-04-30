"""Solves sudoku puzzles"""

import time
from grid import Grid, Cell


def debug_print_board(grid, debug):
	"""Prints grid and sleeps .5sec if debug True"""
	if debug:
		print(grid)
		print("\n\n")
		time.sleep(.5)
