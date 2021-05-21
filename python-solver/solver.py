"""Solves sudoku puzzles"""

import time
from grid import Grid, Cell
from puzzles import easy_puzzles, medium_puzzles, expert_puzzles


def debug_print_board(grid, debug):
	"""Prints grid and sleeps .5sec if debug True"""
	if debug:
		print(grid)
		print("\n\n")
		time.sleep(.5)

def solve(grid, debug=False):
	while len(grid.solved_cells) < 81:
		board_unchanged = False
		for solved in grid.solved_cells:
			for unsolved in filter(lambda x: not x.digit, solved.neighbors):
				if solved.digit in unsolved.possibilities:
					unsolved.remove_possibility(solved.digit)
					board_unchanged = True
				if len(unsolved.possibilities) == 1:
					unsolved.set_digit(unsolved.possibilities[0])
					board_unchanged = True
					debug_print_board(grid, debug)
		stuck = not board_unchanged
	print("Solved:")
	print(grid)
	print("\n\n")

if __name__ == "__main__":
	grid = Grid(medium_puzzles[0], True)
	print("Unsolved:")
	print(grid)
	print("\n\n")
	solve(grid, True)
