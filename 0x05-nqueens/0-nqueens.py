#!/usr/bin/python3
"""
NQueens
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for i in range(row):
        if board[i] == col or abs(i - row) == abs(board[i] - col):
            return False
    return True


def solve_n_queens(n):
    """
    Solve the N queens problem and print solutions
    """
    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    chessboard = [-1] * n
    solutions = []

    def backtrack(row_idx):
        """
        Backtracking to find all possible solutions
        """
        if row_idx == n:
            solutions.append([[i, chessboard[i]] for i in range(n)])
        else:
            for col_idx in range(n):
                if is_safe(chessboard, row_idx, col_idx):
                    chessboard[row_idx] = col_idx
                    backtrack(row_idx + 1)
                    chessboard[row_idx] = -1

    backtrack(0)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        n_queens = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    solve_n_queens(n_queens)
