from kenken.board import Board
from kenken.solver import solve

def main():
    size = 10  # Example size for a 10X10 KenKen board
    board = Board(size)
    solve(board)
    if board.is_solved():
        board.display()
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()