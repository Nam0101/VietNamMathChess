import numpy as np

from ultils.variable import COLUMN, square_values
from ultils.variable import ROW
from ultils.variable import cols_to_files
from ultils.variable import piece_score
from ultils.variable import rows_to_ranks


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
        self.checkmate = 50
        self.stalemate = 0

    def evaluation(self, state):
        score = 0
        red_good_index = 0
        blue_good_index = 0
        board = state.board
        checkmate = self.checkmate
        red_score = 45
        blue_score = 45
        red_rows, red_cols = np.where(np.char.startswith(board, "r"))
        for row, col in zip(red_rows, red_cols):
            piece = board[row, col]
            square = getRankFile(row, col)
            red_good_index += square_values.get(square, 0)
            if int(piece[1]) == 0:
                score += checkmate
            else:
                score += piece_score[piece[1]]
                red_score -= int(piece[1])
        blue_rows, blue_cols = np.where(np.char.startswith(board, "b"))
        for row, col in zip(blue_rows, blue_cols):
            piece = board[row, col]
            square = getRankFile(row, col)
            blue_good_index += square_values.get(square, 0)
            if int(piece[1]) == 0:
                score -= checkmate
            else:
                score -= piece_score[piece[1]]
                blue_score -= int(piece[1])
        if red_score > 25:
            score += checkmate
        elif blue_score > 25:
            score -= checkmate
        return score + (red_good_index - blue_good_index) * 0.2

    def evaluate_move(self, move, state):
        multi = 1 if state.red_turn else -1
        score = 0
        piece_captured = move.piece_captured
        if piece_captured[0] == "r":
            if piece_captured[1] == "0":
                score += multi * self.checkmate
            else:
                score += multi * int(piece_captured[1])
        elif piece_captured[0] == "b":
            if piece_captured[1] == "0":
                score += multi * -self.checkmate
            else:
                score += -multi * int(piece_captured[1])
        square = getRankFile(move.end_row, move.end_col)
        square_value = square_values.get(square)
        if square_value is not None:
            score += multi * square_value
        return score

    def AI_move(self):
        raise NotImplementedError

    def AI_find_move(self, statement, valid_moves):
        raise NotImplementedError

    def quiesce(self, alpha, beta, state):
        stand_pat = self.evaluation(state)
        if stand_pat >= beta:
            return beta
        if alpha < stand_pat:
            alpha = stand_pat
        valid_moves = state.get_all_attack_move()
        for player_move in valid_moves:
            state.make_move(player_move)
            score = -self.quiesce(-beta, -alpha, state)
            state.undo_move()
            if score >= beta:
                return beta
            if score > alpha:
                alpha = score
        return alpha
