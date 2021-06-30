"""Solves sudoku puzzles"""

import time
import copy
from grid import Grid, Cell
from puzzles import easy_puzzles, medium_puzzles, expert_puzzles, unsolvable_puzzles


def debug_print_board(grid, debug):
	"""Prints grid and sleeps .5sec if debug True"""
	if debug:
		print(grid)
		print("\n\n")
		# time.sleep(.5)

def solve(grid, debug=False):
	while len(grid.solved_cells) < 81:
		board_unchanged = True
		for solved in grid.solved_cells:
			for unsolved in filter(lambda x: not x.digit, solved.neighbors):
				if len(unsolved.possibilities) == 0:
					raise Exception("Impossible grid state, reverting to before last guess")
				if solved.digit in unsolved.possibilities:
					unsolved.remove_possibility(solved.digit)
					board_unchanged = False
				if len(unsolved.possibilities) == 1:
					unsolved.set_digit(unsolved.possibilities[0])
					board_unchanged = False
					debug_print_board(grid, debug)
		if board_unchanged:
			print("Starting guessing algorithm")
			for unsolved in grid.unsolved_cells:
				# find an unsolved cell with only 2 possibilities
				if len(unsolved.possibilities) == 2:
					# create a copy of grid to test a guess
					grid1 = copy.deepcopy(grid)
					# guess first possibility
					guess = unsolved.possibilities[0]
					grid1.graph[unsolved.coordinates].set_digit(guess)
					try:
						print("Making guess:")
						debug_print_board(grid1, debug)
						return solve(grid1, debug)
					except Exception as e: # first guess was incorrect
						print(e)
						# create a copy of grid to test a guess
						grid2 = copy.deepcopy(grid)
						# guess second  possibility
						guess = unsolved.possibilities[1]
						grid2.graph[unsolved.coordinates].set_digit(guess)
						
						print("Making second guess")
						debug_print_board(grid2, debug)
						return solve(grid2, debug)
			return grid
	return grid

if __name__ == "__main__":
	grid = Grid(medium_puzzles[0])
	print("Unsolved:")
	print(grid)
	print("\n\n")
	grid = solve(grid, True)
	try:
		print("Solved:")
		print(grid)
	except Exception as e:
		print("Unable to solve:")
		print(grid)
