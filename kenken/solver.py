"""Module to solve KenKen puzzles.
"""
def solve(board):
    """ Solve the KenKen puzzle represented by the board.
    """
    board.generate_constraints()
    def inner_solve():
        if board.is_solved():
            return True # Solved!
        unsolved_cells = board.get_unsolved_cells()
        unsolved_cells.sort(key=lambda cell: len(board.get_constraint(cell))) #heuristic most constarined cell first
        cell = unsolved_cells[0]
        for val in board.get_constraint(cell):
            board.set_cell(cell, val)
            if inner_solve():
                return True
            board.unset_cell(cell)
        return False
    inner_solve()

