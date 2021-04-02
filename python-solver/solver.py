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

class Grid:
	"""A full sudoku grid"""
	def __init__(self, hints={}):
		self.graph = self.create_graph()
		self.fill_hints(hints)

	def create_graph(self):
		"""Creates 81 cells, and a graph where every cell is a node connected to every other cell in a group with it.
		Returns a dictionary
		"""
		pass
	def create_cell(self, x, y):
		"""Creates a Cell at (x, y)"""
		return Cell(x, y)

	def fill_hints(self, hints):
		"""Fills hints into grid.
		Expects dictionary in the form of {(int, int): int}
		"""
		pass
