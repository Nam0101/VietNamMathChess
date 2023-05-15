import state.state as state

piece_score = {'0': 100, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 8, '7': 10, '8': 15, '9': 20}

COLUMN = 9
ROW = 11
CHECKMATE = 168


class StateEvaluation:
    def __init__(self):
        self.checkmate = 45
        self.stalemate = 0
        self.turnMultiplier = 1 if self.state.red_turn else -1

    def evaluation(self,board):
        score = 0
        for row in board:
            for square in row:
                if square[0] == "r":
                    if int(square[1]) == 0:
                        score += self.checkmate
                    else:
                        score += int(square[1])
                elif square[0] == "b":
                    if int(square[1]) == 0:
                        score -= self.checkmate
                    else:
                        score -= int(square[1])
        return score

    def find_best_move(self):
        self.turnMultiplier = 1 if self.state.red_turn else -1
        valid_moves = self.state.get_all_possible_move()
        max_score = -CHECKMATE
        best_move = None
        for player_move in valid_moves:
            self.state.make_move(player_move, valid_moves)
            score = self.evaluation()
            self.state.undo_move()
            if score > max_score:
                max_score = score
                best_move = player_move
        return best_move

    def minimax(self, dept, alpha, beta, is_maximizing_player):
        if dept == 0 or self.state.is_end():
            return self.turnMultiplier * self.evaluation()

        valid_moves = self.state.get_all_possible_move()
        if is_maximizing_player:
            max_score = -CHECKMATE
            for player_move in valid_moves:
                self.state.make_move(player_move, valid_moves)
                score = self.minimax(dept - 1, alpha, beta, False)
                self.state.undo_move()
                max_score = max(max_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return max_score
        else:
            min_score = CHECKMATE
            for player_move in valid_moves:
                self.state.make_move(player_move, valid_moves)
                score = self.minimax(dept - 1, alpha, beta, True)
                self.state.undo_move()
                min_score = min(min_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return min_score

    def minimax_move(self, dept, is_maximizing_player):
        valid_moves = self.state.get_all_possible_move()
        max_score = -CHECKMATE
        best_move = None
        for player_move in valid_moves:
            self.state.make_move(player_move, valid_moves)
            score = self.minimax(dept - 1, -CHECKMATE, CHECKMATE, is_maximizing_player)
            self.state.undo_move()
            if score > max_score:
                max_score = score
                best_move = player_move
        return best_move
