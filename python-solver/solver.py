"""Solves sudoku puzzlse"""

class Cell:
	"""One cell on a grid"""
	def __init__(self, x, y):
		self.digit = None
		self.coordinates = (x, y)
		self.possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	def set_digit(self, n):
		"""Set self.digit to n"""
		self.digit = n

	def remove_possibility(self, n):
		"""Remove n from self.possibilities, return self.possibilities.
		Expects an int, returns a list
		"""
		# Raises a ValueError if n not in self.possibilities
		i = self.possibilities.index(n)
		# Removes n from self.possibilities
		self.possibilities = self.possibilities[:i] + self.possibilities[i+1:]
		return self.possibilities
