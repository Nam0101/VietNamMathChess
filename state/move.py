from ultils.variable import cols_to_files
from ultils.variable import rows_to_ranks


class Move:
    def __init__(self, start_square, end_square, board):
        self.start_row = start_square[0]
        self.start_col = start_square[1]
        self.end_row = end_square[0]
        self.end_col = end_square[1]
        self.piece_moved = board[self.start_row, self.start_col]
        self.piece_captured = board[self.end_row, self.end_col]
        self.move_ID = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col
        self.is_attack = self.evaluate_attack()

    def getChessNotation(self):
        return self.getRankFile(self.start_row, self.start_col) + self.getRankFile(self.end_row, self.end_col)

    @staticmethod
    def getRankFile(r, c):
        return cols_to_files[c] + rows_to_ranks[r]

    def evaluate_attack(self):
        return self.piece_captured != "--"

    # override equals method
    def __eq__(self, other):
        return isinstance(other, Move) and self.move_ID == other.move_ID

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
