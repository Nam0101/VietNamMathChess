import itertools
import time

from ai.AI import AI
from ai.Zobrist_hash import Zobrist_hash


class Negamax(AI):
    def __init__(self, depth):
        super().__init__()
        self.zh = Zobrist_hash()
        self.result_move = None
        self.DEPTH = depth
        self.state_visited = 0
        self.transposition_table = {}
        self.state_found = 0

    def evaluation(self, state):
        evaluation = super().evaluation(state)
        return evaluation

    def negamax_alpha_beta(self, state, depth, alpha, beta, turn_multiplier):
        self.state_visited += 1
        if depth == 0 or state.game_over():
            zobrist_hash = self.zh.calculate_zobrist_hash(state.board)
            if zobrist_hash in self.transposition_table:
                self.state_found += 1
                return self.transposition_table[zobrist_hash]
            else:
                evaluation = turn_multiplier * self.evaluation(state)
                self.transposition_table[zobrist_hash] = evaluation
                return evaluation
        max_score = -self.checkmate
        valid_moves = state.get_all_possible_move()
        sorted_moves = (player_move for player_move in
                        sorted(valid_moves, key=lambda moves: self.evaluate_move(moves, state),
                               reverse=state.red_turn))
        for move in sorted_moves:
            state.make_move(move)
            score = -self.negamax_alpha_beta(state, depth - 1, -beta, -alpha,
                                             -turn_multiplier)
            if score > max_score:
                max_score = score
                if depth == self.DEPTH:
                    self.result_move = move
            alpha = max(alpha, score)
            state.undo_move()
            if alpha >= beta:
                break
        return max_score

    def findMove(self, statement, valid_moves):
        start_time = time.time()
        self.result_move = None
        print("Finding moves with negamax, depth = ", self.DEPTH, "...")
        score = self.negamax_alpha_beta(statement, self.DEPTH, -self.checkmate, self.checkmate,
                                        1 if statement.red_turn else -1)
        end_time = time.time()
        print("Time used: ", end_time - start_time)
        print("Score:", score)
        print("State visited:", self.state_visited)
        print("Transposition table size:", len(self.transposition_table),
              " states found in table: " + str(self.state_found))
        self.state_visited = 0
        return self.result_move
