"""Solves sudoku puzzles"""

import time
from grid import Grid, Cell


def debug_print_board(grid, debug):
	"""Prints grid and sleeps .5sec if debug True"""
	if debug:
		print(grid)
		print("\n\n")
		time.sleep(.5)

def solve(hints, debug=False):
	grid = Grid(hints)
	print("Unsolved:")
	print(grid)
	print("\n\n")
	while len(grid.solved_cells) < 81:
		for solved in grid.solved_cells:
			for unsolved in filter(lambda x: not x.digit, solved.neighbors):
				if solved.digit in unsolved.possibilities:
					unsolved.remove_possibility(solved.digit)
				if len(unsolved.possibilities) == 1:
					unsolved.set_digit(unsolved.possibilities[0])
					debug_print_board(grid, debug)
	print("Solved:")
	print(grid)
	print("\n\n")

