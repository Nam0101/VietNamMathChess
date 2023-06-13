from numba import jit

piece_score = {'0': 100, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

COLUMN = 9
ROW = 11

ranks_to_rows = {"1": 10, "2": 9, "3": 8, "4": 7, "5": 6, "6": 5,
                 "7": 4, "8": 3, "9": 2, "10": 1, "11": 0}
rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4,
                 "f": 5, "g": 6, "h": 7, "i": 8}
cols_to_files = {v: k for k, v in files_to_cols.items()}


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


# def evaluation_piece_near_king(board, red_turn):
#     square_values = {"e4": 2, "e5": 2, "d4": 2, "d5": 2, "c6": 1, "d6": 1, "e6": 1, "f6": 1,
#                      "c3": 1, "d3": 1, "e3": 1, "f3": 1, "c4": 1, "c5": 1, "f4": 1, "f5": 1}
#     score = 0
#     for row in range(ROW):
#         for col in range(COLUMN):
#             if red_turn:
#                 if board[row][col][0] == "r":
#                     square = getRankFile(row, col)
#                     if square in square_values:
#                         score += square_values[square]
#             else:
#                 if board[row][col][0] == "b":
#                     square = getRankFile(row, col)
#                     if square in square_values:
#                         score += square_values[square]
#     return score


class AI:
    def __init__(self):
        self.DEPTH = None
        self.next_move = None
        self.checkmate = 100
        self.stalemate = 0

    # def evaluation(self, state):
    #     score = 0
    #     for row in state.board:
    #         for square in row:
    #             if square[0] == "r":
    #                 if int(square[1]) == 0:
    #                     score += self.checkmate
    #                 else:
    #                     score += piece_score[square[1]]
    #             elif square[0] == "b":
    #                 if int(square[1]) == 0:
    #                     score -= self.checkmate
    #                 else:
    #                     score -= piece_score[square[1]]
    #     return score + 0.5 * evaluation_piece_near_king(state.board, True) - 0.5 * evaluation_piece_near_king(
    #         state.board, False)
    def evaluation(self, state):
        square_values = {"e4": 2, "e5": 2, "d4": 2, "d5": 2, "c6": 1, "d6": 1, "e6": 1, "f6": 1,
                         "c3": 1, "d3": 1, "e3": 1, "f3": 1, "c4": 1, "c5": 1, "f4": 1, "f5": 1}
        score = 0
        red_score = 0
        blue_score = 0
        for row in range(ROW):
            for col in range(COLUMN):
                if state.board[row][col][0] == "r":
                    if state.red_turn:
                        square = getRankFile(row, col)
                        if square in square_values:
                            red_score += square_values[square]
                    if int(state.board[row][col][1]) == 0:
                        score += self.checkmate
                    else:
                        score += piece_score[state.board[row][col][1]]
                elif state.board[row][col][0] == "b":
                    if not state.red_turn:
                        square = getRankFile(row, col)
                        if square in square_values:
                            blue_score += square_values[square]
                    if int(state.board[row][col][1]) == 0:
                        score -= self.checkmate
                    else:
                        score -= piece_score[state.board[row][col][1]]
        return score + 0.5 * red_score - 0.5 * blue_score

    def AI_move(self):
        raise NotImplementedError

    def findMove(self, statement, valid_moves):
        raise NotImplementedError

