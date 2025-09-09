"""
Module for KenKen board representation.
"""

from dataclasses import dataclass

from collections import namedtuple
Cell = namedtuple("cell", ["row", "col"])

dataclass(frozen=True)
class Rule:
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
        self.__size = size
        self.__grid = [["*" for _ in range(size)] for _ in range(size)]
        self.__rules = []
        self.__constraints_set = False
    
    def display(self):
        """ Display the board in a readable format.
        """
        for row in self.__grid:
            print(" | ".join(str(cell) if cell != "*" else "." for cell in row))
            print("-" * (self.__size * 4 - 1))
        


    def add_rule(self, rule):
        pass

    def generate_constraints(self):
        """generate constraints based on rules, for now simple soduku style constraints
        """
        self.__row_constrainsts = [set(range(1, self.__size + 1)) for _ in range(self.__size)]
        self.__col_constraints = [set(range(1, self.__size + 1)) for _ in range(self.__size)]
        self.__constraints_set = True


    def get_constraint(self, cell):
        assert self.__constraints_set
        assert isinstance(cell, Cell)
        assert 0 <= cell.row < self.__size
        assert 0 <= cell.col < self.__size
        return self.__row_constrainsts[cell.row] & self.__col_constraints[cell.col]
    
    def set_cell(self, cll, val):
        assert isinstance(cll, Cell)
        assert 0 <= cll.row < self.__size
        assert 0 <= cll.col < self.__size
        assert 1 <= val <= self.__size
        assert self.__grid[cll.row][cll.col] == "*"
        assert val in self.get_constraint(cll)
        self.__row_constrainsts[cll.row].discard(val)
        self.__col_constraints[cll.col].discard(val)
        self.__grid[cll.row][cll.col] = val

    def unset_cell(self, cell):
        assert isinstance(cell, Cell)
        assert 0 <= cell.row < self.__size
        assert 0 <= cell.col < self.__size
        val = self.__grid[cell.row][cell.col]
        assert val != "*"
        self.__row_constrainsts[cell.row].add(val)
        self.__col_constraints[cell.col].add(val)
        self.__grid[cell.row][cell.col] = "*"
    
    def get_unsolved_cells(self):
        return [Cell(r, c) for r in range(self.__size) for c in range(self.__size) if self.__grid[r][c] == "*"]
    
    def is_solved(self):
        return all(self.__grid[r][c] != "*" for r in range(self.__size) for c in range(self.__size))





    