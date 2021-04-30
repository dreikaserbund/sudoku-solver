"""Sudoku puzzle grid"""

class Cell:
    """One cell on a grid"""
    def __init__(self, x, y, grid):
        self.grid = grid
        self.digit = None
        self.coordinates = (x, y)
        self.possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.neighbors = list()

    def set_digit(self, n):
        """Set self.digit to n"""
        self.digit = n
        # adds self to list of solved cells in the grid
        self.grid.solved_cells.append(self)

    def remove_possibility(self, n):
        """Remove n from self.possibilities, return self.possibilities.
        Expects an int, returns a list
        """
        # Raises a ValueError if n not in self.possibilities
        i = self.possibilities.index(n)
        # Removes n from self.possibilities
        self.possibilities = self.possibilities[:i] + self.possibilities[i+1:]
        return self.possibilities

    def add_neighbor(self, cell):
        if not ((cell is self) or (cell in self.neighbors)):
            self.neighbors.append(cell)

class Grid:
    """A full sudoku grid"""
    def __init__(self, hints={}):
        self.graph = dict()
        self.solved_cells = list()
        self.create_graph()
        self.set_all_connections()
        self.fill_hints(hints)

    def __str__(self):
        """Returns a ascii art of the gridstate"""
        # list of all digits in the grid as strings, with filler for an empty digit
        grid_list = list()
        # used in place of an empty cell
        filler = "."
        for y in range(9):
            for x in range(9):
                digit_int = self.graph[(x,y)].digit
                if digit_int:
                    grid_list.append(digit_int)
                else:
                    grid_list.append(filler)
        return "{} {} {}|{} {} {}|{} {} {}\n{} {} {}|{} {} {}|{} {} {}\n{} {} {}|{} {} {}|{} {} {}\n-----+-----+-----\n{} {} {}|{} {} {}|{} {} {}\n{} {} {}|{} {} {}|{} {} {}\n{} {} {}|{} {} {}|{} {} {}\n-----+-----+-----\n{} {} {}|{} {} {}|{} {} {}\n{} {} {}|{} {} {}|{} {} {}\n{} {} {}|{} {} {}|{} {} {}".format(*grid_list)

    def create_graph(self):
        """Creates 81 cells, and a graph where every cell is a node connected to every other cell in a group with it.
        Returns a dictionary
        """
        for x in range(9):
            for y in range(9):
                self.graph[(x, y)] = self.create_cell(x, y)

    def create_cell(self, x, y):
        """Creates a Cell at (x, y)"""
        return Cell(x, y, self)

    def fill_hints(self, hints):
        """Fills hints into grid.
        Expects dictionary in the form of {(int, int): int}
        """
        for coord, digit in hints.items():
            self.graph[coord].set_digit(digit)

    def set_all_connections(self):
        for x in range(9):
            for y in range(9):
                cell = self.graph[(x, y)]
                self.set_outward_connections(cell)

    def set_outward_connections(self, cell):
        x, y = cell.coordinates
        for n in range(9):
            cell.add_neighbor(self.graph[(x, n)])
            cell.add_neighbor(self.graph[(n, y)])
        bx, by = (x//3*3), (y//3*3) # start x and y of cell's block
        for a in range(bx, bx+3):
            for b in range(by, by+3):
                cell.add_neighbor(self.graph[(a, b)])
