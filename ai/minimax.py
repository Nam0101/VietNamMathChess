import time

from ai.AI import AI
from ultils.Zobrist_hash import zobrist_hash


class minimax(AI):
    def __init__(self, depth):
        super().__init__()
        self.state_found = 0
        self.DEPTH = depth
        self.next_move = None
        self.state_visited = 0
        self.MAX_TIME = 10
        self.transposition_table = {}
        self.zh = zobrist_hash()
        self.move_log = []

    def evaluation(self, state):
        evaluation = super().evaluation(state)
        return evaluation

    def minimax_move(self, depth, state, alpha, beta, maximizingPlayer, start_time):
        self.state_visited += 1
        if depth == 0 or state.game_over():
            zobrist_hash = self.zh.calculate_zobrist_hash(state.board)
            if zobrist_hash in self.transposition_table:
                self.state_found += 1
                return self.transposition_table[zobrist_hash]
            else:
                evaluation = self.evaluation(state)
                self.transposition_table[zobrist_hash] = evaluation
                return evaluation
        if maximizingPlayer:
            max_score = -self.checkmate
            valid_moves = state.get_all_valid_move()
            sorted_moves = (player_move for player_move in
                            sorted(valid_moves, key=lambda moves: self.evaluate_move(moves, state),
                                   reverse=state.red_turn))
            # only move 50% best move
            # moves_to_consider = itertools.islice(sorted_moves, int(.7 * len(valid_moves)))
            for move in sorted_moves:
                # print(evaluate_move(move, state))
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
            valid_moves = state.get_all_valid_move()
            sorted_moves = (player_move for player_move in
                            sorted(valid_moves, key=lambda moves: self.evaluate_move(moves, state),
                                   reverse=state.red_turn))
            # moves_to_consider = itertools.islice(sorted_moves, int(0.7 * len(valid_moves)))
            for move in sorted_moves:
                # print(evaluate_move(move, state))
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

    def minimax_move_noAlphaBeta(self, depth, state, maximizingPlayer):
        self.state_visited += 1
        if depth == 0 or state.game_over():
            zobrist_hash = self.zh.calculate_zobrist_hash(state.board)
            if zobrist_hash in self.transposition_table:
                self.state_found += 1
                return self.transposition_table[zobrist_hash]
            else:
                evaluation = self.evaluation(state)
                self.transposition_table[zobrist_hash] = evaluation
                return evaluation
        if maximizingPlayer:
            max_score = -self.checkmate
            valid_moves = state.get_all_valid_move()
            sorted_moves = (player_move for player_move in
                            sorted(valid_moves, key=lambda moves: self.evaluate_move(moves, state),
                                   reverse=state.red_turn))
            for move in sorted_moves:
                state.make_move(move)
                eval_score = self.minimax_move_noAlphaBeta(depth - 1, state, False)
                state.undo_move()
                if eval_score > max_score:
                    max_score = eval_score
                    if depth == self.DEPTH:
                        self.next_move = move
            return max_score
        else:
            min_score = self.checkmate
            valid_moves = state.get_all_valid_move()
            sorted_moves = (player_move for player_move in
                            sorted(valid_moves, key=lambda moves: self.evaluate_move(moves, state),
                                   reverse=state.red_turn))
            for move in sorted_moves:
                state.make_move(move)
                eval_score = self.minimax_move_noAlphaBeta(depth - 1, state, True)
                state.undo_move()
                if eval_score < min_score:
                    min_score = eval_score
                    if depth == self.DEPTH:
                        self.next_move = move
            return min_score

    def AI_find_move(self, state, valid_moves):
        alpha = -self.checkmate
        beta = self.checkmate
        print("Finding moves with AlphaBeta, depth = ", self.DEPTH, "...")
        start_time = time.time()
        score = self.minimax_move(self.DEPTH, state, alpha, beta, state.red_turn, start_time)
        # score = self.minimax_move_noAlphaBeta(2, state, state.red_turn)
        # score = self.mtdf(0, self.DEPTH, state)
        end_time = time.time()
        print("Time used: ", end_time - start_time)
        print("Score:", score)
        print("State visited:", self.state_visited)
        print("Transposition table size:", len(self.transposition_table),
              " states found in table: " + str(self.state_found))
        self.state_visited = 0
        self.move_log.append(self.next_move)
        if self.next_move is None:
            sorted_moves = sorted(valid_moves, key=lambda move: self.evaluation(state), reverse=True)
            return sorted_moves[-1]
        return self.next_move
