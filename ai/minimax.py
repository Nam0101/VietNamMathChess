import random

from ai.AI import AI


class minnimax(AI):
    def __int__(self):
        super().__init__()

    def evaluation(self):
        evaluation = super().evaluation()
        return evaluation

    def minimax(self, depth, state, alpha, beta, maximizingPlayer):
        if depth == 0 or state.game_over():
            return self.evaluation()
        if maximizingPlayer:
            maxEval = -self.checkmate
            for move in state.get_all_possible_move():
                state.make_move(move, state.get_all_possible_move())
                eval = self.minimax(depth - 1, state, alpha, beta, False)
                state.undo_move()
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = self.checkmate
            for move in state.get_all_possible_move():
                state.make_move(move, state.get_all_possible_move())
                eval = self.minimax(depth - 1, state, alpha, beta, True)
                state.undo_move()
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return minEval

    def findMove(self, valid_moves):
        turn_multiplier = 1 if self.Statement.red_turn else -1
        max_score = -self.checkmate
        best_move = None
        random.shuffle(valid_moves)
        for player_move in valid_moves:
            self.Statement.make_move(player_move, valid_moves)
            score = turn_multiplier * self.minimax(1, self.Statement, -self.checkmate, self.checkmate, True)
            if score > max_score:
                max_score = score
                best_move = player_move
            self.Statement.undo_move()
        return best_move
