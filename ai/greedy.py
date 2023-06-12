import random

from ai.AI import AI

current_state = None


class greedy(AI):
    def __init__(self):
        super().__init__()

    def evaluation(self, state):
        evaluation = super().evaluation(state)
        return evaluation

    def findMove(self, statement, valid_moves, depth=0):
        turn_multiplier = 1 if statement.red_turn else -1
        max_score = -self.checkmate
        best_move = None
        random.shuffle(valid_moves)
        for player_move in valid_moves:
            statement.make_move(player_move)
            score = turn_multiplier * self.evaluation(statement)
            if score > max_score:
                max_score = score
                best_move = player_move
            statement.undo_move()
        return best_move
