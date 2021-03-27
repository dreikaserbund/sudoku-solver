"""Solves sudoku puzzlse"""

class Cell:
	"""One cell on a grid"""
	def __init__(self, x, y):
		self.digit = None
		self.coordinates = (x, y)
		self.possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
