#!/usr/bin/python3
"""N Queens"""
import sys


def print_board(board, n):
    """Print allocated positions to the queen"""
    b = []
    for i in range(n):
        b.append([i, board[i]])
    print(b)


def is_position_safe(board, i, j, row):
    """Checks if the position is safe for the queen"""
    return board[i] == j or board[i] == j - i + row or board[i] == i - row + j


def safe_positions(board, row, n):
    """Find all safe positions where the queen can be allocated"""
    if row == n:
        print_board(board, n)
    else:
        for j in range(n):
            if all(not is_position_safe(board, i, j, row) for i in range(row)):
                board[row] = j
                safe_positions(board, row + 1, n)


def create_board(size):
    """Generates the board"""
    return [0] * size


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

board = create_board(n)
safe_positions(board, 0, n)
