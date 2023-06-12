import random

from ai.AI import AI

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import time


def evaluate_move(move, red_play):
    multi = 1 if red_play else -1
    if move.piece_moved[0] == "r":
        if move.piece_moved[1] == "0":
            return multi * 100
        else:
            return multi * int(move.piece_moved[1])
    elif move.piece_moved[0] == "b":
        if move.piece_moved[1] == "0":
            return multi * -100
        else:
            return -multi * int(move.piece_moved[1])
    else:
        return 0


class minimax(AI):
    def __init__(self, depth):
        super().__init__()
        self.DEPTH = depth
        self.next_move = None

    def evaluation(self, state):
        evaluation = super().evaluation(state)
        return evaluation

    def minimax_move(self, depth, state, alpha, beta, maximizingPlayer):
        if depth == 0 or state.game_over():
            # print("Current score: ", self.evaluation(state.board))
            return self.evaluation(state)
        if maximizingPlayer:
            max_score = -self.checkmate
            valid_moves = state.get_all_possible_move()
            sorted_moves = sorted(valid_moves, key=lambda moves: evaluate_move(moves, state.red_turn),
                                  reverse=maximizingPlayer)
            for move in sorted_moves:
                state.make_move(move)
                eval_score = self.minimax_move(depth - 1, state, alpha, beta, False)
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
                state.make_move(move)
                eval_score = self.minimax_move(depth - 1, state, alpha, beta, True)
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
        random.shuffle(valid_moves)
        print("Finding moves with minimax, depth = ", self.DEPTH, "...")
        start_time = time.time()
        score=self.minimax_move(self.DEPTH, state, alpha, beta, state.red_turn)
        end_time = time.time()
        print("Time used:", end_time - start_time)
        print("Score:", score)
        return self.next_move
