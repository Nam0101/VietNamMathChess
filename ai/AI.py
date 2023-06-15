import time

import numpy as np
from numba import jit

from ai.variable import square_values
from ai.variable import piece_score
from ai.variable import COLUMN
from ai.variable import ROW
from ai.variable import ranks_to_rows
from ai.variable import files_to_cols
from ai.variable import rows_to_ranks
from ai.variable import cols_to_files
from state.state import State


def getRankFile(r, c):
    return cols_to_files[c] + rows_to_ranks[r]


def getChessNotation(start_row, start_col, end_row, end_col):
    return getRankFile(start_row, start_col) + getRankFile(end_row, end_col)


def in_check(state):
    # check if the opponent can attack the king, king is at board[1][4] if red turn, board[9][4] if blue turn
    if state.red_turn:
        king_row = 1
        king_col = 4
    else:
        king_row = 9
        king_col = 4
    # check for all opponent pieces if they can attack the king
    for row in range(ROW):
        for col in range(COLUMN):
            if state.board[row][col][0] == "b" and state.red_turn:
                attack_moves = state.get_all_attack_move()
                for move in attack_moves:
                    if move.end_row == king_row and move.end_col == king_col:
                        print("red in check")
                        return True
            elif state.board[row][col][0] == "r" and not state.red_turn:
                attack_moves = state.get_all_attack_move()
                for move in attack_moves:
                    if move.end_row == king_row and move.end_col == king_col:
                        print("blue in check")
                        return True


class AI:
    def __init__(self):
        self.DEPTH = None
        self.next_move = None
        self.checkmate = 100
        self.stalemate = 0

    def evaluation(self, state):
        square_values = {"e4": 2, "e5": 2, "d4": 2, "d5": 2, "c6": 1, "d6": 1, "e6": 1, "f6": 1,
                         "c3": 1, "d3": 1, "e3": 1, "f3": 1, "c4": 1, "c5": 1, "f4": 1, "f5": 1}
        score = 0
        red_score = 0
        blue_score = 0
        for row in range(ROW):
            for col in range(COLUMN):
                piece = state.board[row, col]
                if piece[0] == "r":
                    if state.red_turn:
                        square = getRankFile(row, col)
                        red_score += square_values.get(square, 0)
                    if int(piece[1]) == 0:
                        score += self.checkmate
                    else:
                        score += piece_score[piece[1]]
                elif piece[0] == "b":
                    if not state.red_turn:
                        square = getRankFile(row, col)
                        blue_score += square_values.get(square, 0)
                    if int(piece[1]) == 0:
                        score -= self.checkmate
                    else:
                        score -= piece_score[piece[1]]
        # red_possible_moves = len(state.get_all_possible_move())
        # state.red_turn = not state.red_turn
        # blue_possible_moves = len(state.get_all_possible_move())
        # state.red_turn = not state.red_turn
        # possible_move = red_possible_moves - blue_possible_moves if state.red_turn else blue_possible_moves - red_possible_moves
        return score + 0.5 * red_score - 0.5 * blue_score

    def AI_move(self):
        raise NotImplementedError

    def findMove(self, statement, valid_moves):
        raise NotImplementedError


