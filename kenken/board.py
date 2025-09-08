"""
Module for KenKen board representation.
"""

class _Rule:
    """
    Class representing a rule in KenKen.
    """
    def __init__(self, cells, target, operation):
        self.cells = cells  # List of (row, col) tuples
        self.target = target  # Target number for the rule
        self.operation = operation  # Operation: '+', '-', '*', '/'


class Board:
    """ 
    Class representing a KenKen board.
    """
    def __init__(self, size):
        self.size = size
        self.grid = [["*" for _ in range(size)] for _ in range(size)]
    
    def display(self):
        """ Display the board in a readable format.
        """
        for row in self.grid:
            print(" ".join(str(cell) for cell in row), end="")

    def add_rule(self, rule):
        pass


    