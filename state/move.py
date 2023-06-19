from numba import int64, boolean
from numba.experimental import jitclass

import numpy as np
from ai.variable import COLUMN
from ai.variable import ROW
from ai.variable import piece_score
from ai.variable import square_values
from ai.variable import ranks_to_rows
from ai.variable import files_to_cols
from ai.variable import rows_to_ranks
from ai.variable import cols_to_files


class Move:
    # map key to value
    # key : value

    def __init__(self, start_square, end_square, board):
        self.start_row = start_square[0]
        self.start_col = start_square[1]
        self.end_row = end_square[0]
        self.end_col = end_square[1]
        self.piece_moved = board[self.start_row, self.start_col]
        self.piece_captured = board[self.end_row, self.end_col]
        self.move_ID = (self.start_row, self.start_col, self.end_row, self.end_col)
        self.is_attack = self.evaluate_attack()

    def getChessNotation(self):
        return self.getRankFile(self.start_row, self.start_col) + self.getRankFile(self.end_row, self.end_col)

    def getRankFile(self, r, c):
        return cols_to_files[c] + rows_to_ranks[r]

    def evaluate_attack(self):
        if self.piece_captured != "--":
            return True
        else:
            return False

    # override equals method
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.move_ID == other.move_ID

    def to_string(self):
        s = "Move " + self.piece_moved + " from " + self.getRankFile(self.start_row,
                                                                     self.start_col) + " to " + self.getRankFile(
            self.end_row, self.end_col)
        return s

    def checking_move(self, state):
        state.make_move(self)
        if state.board[1, 4] != "b0" or state.board[9, 4] != "r0":
            return True
        state.undo_move()
        return False

    def is_defend_move(self, state, checking):
        if checking:
            state.make_move(self)
            if state.is_check():
                state.undo_move()
                return False
            else:
                state.undo_move()
                return True
        else:
            return False
