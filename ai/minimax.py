import random

from numba import jit

from ai.AI import AI
from ai.AI import ranks_to_rows
from ai.AI import files_to_cols
from ai.AI import rows_to_ranks
from ai.AI import cols_to_files
from ai.AI import ROW
from ai.AI import COLUMN
from ai.AI import getRankFile
from ai.AI import getChessNotation
import time

square_values = {"e4": 2, "e5": 2, "d4": 2, "d5": 2, "c6": 1, "d6": 1, "e6": 1, "f6": 1,
                 "c3": 1, "d3": 1, "e3": 1, "f3": 1, "c4": 1, "c5": 1, "f4": 1, "f5": 1}


def evaluate_move(move, red_play):
    multi = 1 if red_play else -1
    score = 0
    checking = move.in_check()
    if checking:
        score += multi * 100
    if move.piece_captured[0] == "r":
        if move.piece_captured[1] == "0":
            score += multi * 100
        else:
            score += multi * int(move.piece_captured[1])
    elif move.piece_captured[0] == "b":
        if move.piece_captured[1] == "0":
            score += multi * -100
        else:
            score += -multi * int(move.piece_captured[1])
    square = getRankFile(move.end_row, move.end_col)
    if square in square_values:
        score += square_values[square]
    return score


class minimax(AI):
    def __init__(self, depth):
        super().__init__()
        self.DEPTH = depth
        self.next_move = None

    def evaluation(self, state):
        evaluation = super().evaluation(state)
        return evaluation

    def minimax_move(self, depth, state, alpha, beta, maximizingPlayer, start_time):
        if depth == 0 or state.game_over() or time.time() - start_time > 10:
            return self.evaluation(state)
        if maximizingPlayer:
            max_score = -self.checkmate
            valid_moves = state.get_all_possible_move()
            sorted_moves = sorted(valid_moves, key=lambda moves: evaluate_move(moves, state.red_turn),
                                  reverse=maximizingPlayer)
            for move in sorted_moves:
                if evaluate_move(move, state.red_turn) > 50:
                    print("Found a good move: ", move.to_string())
                state.make_move(move)
                eval_score = self.minimax_move(depth - 1, state, alpha, beta, False, start_time)
                state.undo_move()
                if eval_score > max_score:
                    max_score = eval_score
                    if depth == self.DEPTH:
                        self.next_move = move
                    alpha = max(alpha, eval_score)
                    if beta <= alpha:
                        break
            return max_score
        else:
            min_score = self.checkmate
            valid_moves = state.get_all_possible_move()
            sorted_moves = sorted(valid_moves, key=lambda moves: evaluate_move(moves, state.red_turn),
                                  reverse=maximizingPlayer)
            for move in sorted_moves:
                if evaluate_move(move, state.red_turn) > 50:
                    print("Found a good move: ", move.to_string())
                state.make_move(move)
                eval_score = self.minimax_move(depth - 1, state, alpha, beta, True, start_time)
                state.undo_move()
                if eval_score < min_score:
                    min_score = eval_score
                    if depth == self.DEPTH:
                        self.next_move = move
                    beta = min(beta, eval_score)
                    if beta <= alpha:
                        break
            return min_score

    def findMove(self, state, valid_moves):
        alpha = -self.checkmate
        beta = self.checkmate
        print("Finding moves with minimax, depth = ", self.DEPTH, "...")
        start_time = time.time()
        score = self.minimax_move(self.DEPTH, state, alpha, beta, state.red_turn, start_time)
        end_time = time.time()
        print("Time used: ", end_time - start_time)
        print("Score:", score)
        return self.next_move
