"""Module to solve KenKen puzzles.
"""
from heapq import heappop, heapify


def solve(board):
    """ Solve the KenKen puzzle represented by the board.
    """
    board.generate_constraints()
    def inner_solve():
        if board.is_solved():
            return True # Solved!
        unsolved_cells = board.get_unsolved_cells()
        unsolved_cells.sort(key=lambda cell: len(board.get_constraint(cell))) #heuristic most constarined cell first
        cll = unsolved_cells[0]
        for val in board.get_constraint(cll):
            board.set_cell(cll, val)
            if inner_solve():
                return True
            board.unset_cell(cll)
        return False
    inner_solve()

