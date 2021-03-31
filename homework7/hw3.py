"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def is_finished(board: List[List]):
    for i in board:
        if "-" in i:
            return False
    return True


def check_diagonals(board: List[List]):
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]
    return False


def check_rows(board: List[List]):
    for i in range(len(board)):
        if len(set(board[i])) == 1:
            return board[i][0]

    return False


def check_columns(board: List[List]):
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    return False


def tic_tac_toe_checker(board: List[List]) -> str:
    expr = check_diagonals(board) or check_rows(board) or check_columns(board)

    if expr:
        return expr + " wins!"

    if is_finished(board):
        return "draw!"

    return "unfinished!"


# ex = [["-", "-", "o"],
#       ["-", "x", "o"],
#       ["x", "o", "x"]]
#
# ex2 = [["-", "-", "o"],
#        ["-", "o", "o"],
#        ["x", "x", "x"]]
#
# print(tic_tac_toe_checker(ex2))
