import random
import time

import numpy as np

from ai.AI import AI
from ai.AI import COLUMN
from ai.AI import ROW
from ai.AI import getChessNotation
from ai.variable import square_values


class Zobrist_hash:
    def __init__(self):
        self.NUM_PIECES = 20
        self.ROWS = 11
        self.COLS = 9
        self.zobrist_keys = np.zeros((self.ROWS, self.COLS, self.NUM_PIECES), dtype=np.uint64)
        self.initKeys()

    def initKeys(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                for piece in range(self.NUM_PIECES):
                    self.zobrist_keys[row, col, piece] = random.getrandbits(64)

    def calculate_zobrist_hash(self, board):
        hash_value = np.uint64(0)
        for row in range(ROW):
            for col in range(COLUMN):
                piece = board[row, col]
                if piece != "--":
                    piece_index = int(piece[1])
                    if piece[0] == "r":
                        piece_index += 10
                    hash_value ^= self.zobrist_keys[row, col, piece_index]
        return hash_value


def evaluate_move(move, state):
    multi = 1 if state.red_turn else -1
    score = 0

    # Kiểm tra xem quân đã bị ăn hay chưa
    if move.piece_captured[0] == "r":
        # Quân đỏ bị ăn
        if move.piece_captured[1] == "0":
            score += multi * 100
        else:
            score += multi * int(move.piece_captured[1])
    elif move.piece_captured[0] == "b":
        # Quân đen bị ăn
        if move.piece_captured[1] == "0":
            score += multi * -100
        else:
            score += -multi * int(move.piece_captured[1])

    # Kiểm tra giá trị của ô đích nước đi
    square = getChessNotation(move.start_row, move.start_col, move.end_row, move.end_col)
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
        self.transposition_table = {}
        self.zh = Zobrist_hash()

    def evaluation(self, state):
        evaluation = super().evaluation(state)
        return evaluation

    def minimax_move(self, depth, state, alpha, beta, maximizingPlayer, start_time):
        self.state_visited += 1
        if depth == 0 or state.game_over() or time.time() - start_time > 10:
            zobrist_hash = self.zh.calculate_zobrist_hash(state.board)
            if zobrist_hash in self.transposition_table:
                return self.transposition_table[zobrist_hash]
            else:
                evaluation = self.evaluation(state)
                self.transposition_table[zobrist_hash] = evaluation
                return evaluation
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
    def is_quiescent(self, state):
        # check if the state is quiescent
        if state.game_over():
            return True
        if state.check:
            return True

    def findMove(self, state, valid_moves):
        alpha = -self.checkmate
        beta = self.checkmate
        print("Finding moves with minimax, depth = ", self.DEPTH, "...")
        start_time = time.time()
        score = self.minimax_move(self.DEPTH, state, alpha, beta, state.red_turn, start_time)
        end_time = time.time()
        print("Time used: ", end_time - start_time)
        print("Score:", score)
        print("State visited:", self.state_visited)
        print("Transposition table size:", len(self.transposition_table))
        self.state_visited = 0
        return self.next_move
