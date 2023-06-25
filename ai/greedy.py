from ai.AI import AI

current_state = None


class greedy(AI):
    def __init__(self):
        super().__init__()
        self.move_log = []

    def evaluation(self, state):
        evaluation = super().evaluation(state)
        return evaluation

    def AI_find_move(self, statement, valid_moves, depth=0):
        turn_multiplier = 1 if statement.red_turn else -1
        max_score = -self.checkmate
        best_move = None
        valid_moves = statement.get_all_valid_move()
        for player_move in valid_moves:
            if len(self.move_log) > 2:
                if player_move in self.move_log[-len(self.move_log)//2 + 1:]:
                    continue
            statement.make_move(player_move)
            score = turn_multiplier * self.evaluation(statement)
            if score > max_score:
                max_score = score
                best_move = player_move
            statement.undo_move()
        self.move_log.append(best_move)
        return best_move
