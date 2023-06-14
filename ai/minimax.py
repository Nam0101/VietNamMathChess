import random

from numba import jit, njit

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
import copy
from ai.variable import square_values


def evaluate_move(move, state):
    multi = 1 if state.red_turn else -1
    score = 0
    checking = move.in_check()
    state_copy = copy.deepcopy(state)
    defending = move.is_defend_move(state_copy, checking)
    if defending:
        score += multi * 100
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
        self.state_visited = 0
        self.MAX_TIME = 10

    def evaluation(self, state):
        evaluation = super().evaluation(state)
        return evaluation

    def minimax_move(self, depth, state, alpha, beta, maximizingPlayer, start_time):
        self.state_visited += 1
        if depth == 0 or state.game_over() or time.time() - start_time > 10:
            return self.evaluation(state)
        if maximizingPlayer:
            max_score = -self.checkmate
            valid_moves = state.get_all_possible_move()
            sorted_moves = (player_move for player_move in
                            sorted(valid_moves, key=lambda moves: evaluate_move(moves, state),
                                   reverse=state.red_turn))
            for move in sorted_moves:
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
            sorted_moves = (player_move for player_move in
                            sorted(valid_moves, key=lambda moves: evaluate_move(moves, state),
                                   reverse=state.red_turn))
            for move in sorted_moves:
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

    # def findMove(self, state, valid_moves):
    #     alpha = -self.checkmate
    #     beta = self.checkmate
    #     print("Finding moves with iterative deepening...")
    #     start_time = time.time()
    #     current_state = copy.deepcopy(state)
    #     depth = 1
    #     while time.time() - start_time < self.MAX_TIME:
    #         score = self.minimax_move(depth, current_state, alpha, beta, state.red_turn, start_time)
    #         depth += 1
    #     end_time = time.time()
    #     print("Time used:", end_time - start_time)
    #     print("Depth reached:", depth - 1)
    #     print("Score:", score)
    #     print("State visited:", self.state_visited)
    #     self.state_visited = 0
    #     return self.next_move
    def findMove(self, state, valid_moves):
        alpha = -self.checkmate
        beta = self.checkmate
        print("Finding moves with minimax, depth = ", self.DEPTH, "...")
        start_time = time.time()
        current_state = copy.deepcopy(state)
        score = self.minimax_move(self.DEPTH, current_state, alpha, beta, state.red_turn, start_time)
        end_time = time.time()
        print("Time used: ", end_time - start_time)
        print("Score:", score)
        print("State visited:", self.state_visited)
        self.state_visited = 0
        return self.next_move