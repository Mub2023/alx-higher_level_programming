#!/usr/bin/python3
"""solves the N queens problem."""


from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if not argv[1].isdigit():
    print("N must be a number")
    exit(1)
N = int(argv[1])

if N < 4:
    print("N must be at least 4")
    exit(1)


def board_g(board=[]):
    """add column of zeroes to the right of any board about to be tested for
    queen arrangements in that column.
    Args:
    board of (int): 2D list of ints, only as wide as
    needed to test the rightmost column for queen conflicts."""
    if len(board):
        for r in board:
            r.append(0)
    else:
        for r in range(N):
            board.append([0])
    return board


def add(board, r, c):
    """Sets "queen," or 1, to coordinates given in board.
    Args:
    board of (int): 2D list of ints, only as wide as
    r (int): first dimension index
    c (int): second dimension index"""
    board[r][c] = 1


def new_safe(board, r, c):
    """For the board given, checks that for a new queen placed in the rightmost
    column, there are no other "queen"s, or 1 values, in the martix to the
    left, and diagonally up-left and down-left.
    Args:
    board  of (int): 2D list of ints, only as wide as
    needed to test the rightmost column for queen conflicts.
    r (int): first dimension index
    c (int): second dimension index
    """
    a = r
    b = c
    for x in range(1, N):
        if (b - x) >= 0:
            if (a - x) >= 0:
                if board[a - x][b - x]:
                    return False
            if board[a][b - x]:
                return False
            if (a + x) < N:
                if board[a + x][b - x]:
                    return False
    return True


def format_can(candidate):
    """Converts a board (matrix of 1 and 0) into a series of row/column
    indicies of each queen/1.
    Args:
    candidates (list) of (list) of (list) of (int): list of all successful
    solutions for amount of columns last checked
    Attributes:
    alx list of (int): each member list contains the row
    column number for each queen found
    Returns:
    alx, the list of coordinates"""
    alx = []
    for x, att in enumerate(candidate):
        alx.append([])
        for y, r in enumerate(att):
            alx[x].append([])
            for z, c in enumerate(r):
                if c:
                    alx[x][y].append(y)
                    alx[x][y].append(z)
    return alx


candidate = []
candidate.append(board_g())

for c in range(N):
    new_candidate = []

    for matrix in candidate:
        for r in range(N):
            if new_safe(matrix, r, c):
                tp = [line[:] for line in matrix]
                add(tp, r, c)

                if c < N - 1:
                    board_g(tp)
                new_candidate.append(tp)

    candidate = new_candidate

for item in format_can(candidate):
    print(item)
