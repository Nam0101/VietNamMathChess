import random
from ai.AI import AI

current_state = None


class greedy(AI):
    def __init__(self,state):
        super().__init__(state)

    def evaluation(self):
        evaluation = super().evaluation()
        return evaluation

    def findMove(self, valid_moves):
        turn_multiplier = 1 if self.Statement.red_turn else -1
        max_score = -self.checkmate
        best_move = None
        random.shuffle(valid_moves)
        for player_move in valid_moves:
            self.Statement.make_move(player_move, valid_moves)
            score = turn_multiplier * self.evaluation()
            if score > max_score:
                max_score = score
                best_move = player_move
            self.Statement.undo_move()
        return best_move
