import random

piece_score = {'0': 100, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 8, '7': 10, '8': 15, '9': 20}

COLUMN = 9
ROW = 11


class StateEvaluation:
    def __init__(self, current_state):
        self.DEPTH = None
        self.next_move = None
        self.Statement = current_state
        self.checkmate = 45
        self.stalemate = 0
        self.turnMultiplier = 1 if self.Statement.red_turn else -1

    def evaluation(self):
        score = 0
        for row in self.Statement.board:
            for square in row:
                if square[0] == "r":
                    if int(square[1]) == 0:
                        score += self.checkmate
                    else:
                        score += piece_score[square[1]]
                elif square[0] == "b":
                    if int(square[1]) == 0:
                        score -= self.checkmate
                    else:
                        score -= piece_score[square[1]]
        return score

    def findMove(self, valid_moves):
        turn_multiplier = 1 if self.Statement.red_turn else -1
        max_score = -self.checkmate
        best_move = None
        random.shuffle(valid_moves)
        for player_move in valid_moves:
            self.Statement.make_move(player_move, valid_moves)
            score = turn_multiplier * self.evaluation()
            self.Statement.undo_move()
            if score > max_score:
                max_score = score
                best_move = player_move
        return best_move

    def minimax(self, dept, alpha, beta, is_maximizing_player):
        if dept == 0 or self.Statement.is_end():
            return self.turnMultiplier * self.evaluation()

        valid_moves = self.Statement.get_all_possible_move()
        if is_maximizing_player:
            max_score = -self.checkmate
            for player_move in valid_moves:
                self.Statement.make_move(player_move, valid_moves)
                score = self.minimax(dept - 1, alpha, beta, False)
                self.Statement.undo_move()
                max_score = max(max_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return max_score
        else:
            min_score = self.checkmate
            for player_move in valid_moves:
                self.Statement.make_move(player_move, valid_moves)
                score = self.minimax(dept - 1, alpha, beta, True)
                self.Statement.undo_move()
                min_score = min(min_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return min_score

    def minimax_move(self, dept, is_maximizing_player):
        valid_moves = self.Statement.get_all_possible_move()
        max_score = -self.checkmate
        best_move = None
        for player_move in valid_moves:
            # self.Statement.make_move(player_move, valid_moves)
            score = self.minimax(dept, -self.checkmate, self.checkmate, is_maximizing_player)
            # self.Statement.undo_move()
            if score > max_score:
                max_score = score
                best_move = player_move
        return best_move

    def findMove(self, valid_moves, depth):
        random.shuffle(valid_moves)
        self.DEPTH = depth
        alpha = -self.checkmate
        beta = self.checkmate
        self.findMoveMinimax(valid_moves, depth, self.Statement.red_turn, alpha, beta)
        return self.next_move

    def findMoveMinimax(self, valid_moves, depth, red_to_move, alpha, beta):
        if depth == 0 or self.isQuiescent():
            return self.evaluation()
        if red_to_move:
            max_score = -self.checkmate
            for move in valid_moves:
                self.Statement.make_move(move, valid_moves)
                next_moves = self.Statement.get_all_possible_move()
                score = self.findMoveMinimax(next_moves, depth - 1, False, alpha, beta)
                self.Statement.undo_move()
                if score > max_score:
                    max_score = score
                    if depth == self.DEPTH:
                        self.next_move = move
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
            return max_score
        else:
            min_score = self.checkmate
            for move in valid_moves:
                self.Statement.make_move(move, valid_moves)
                next_moves = self.Statement.get_all_possible_move()
                score = self.findMoveMinimax(next_moves, depth - 1, True, alpha, beta)
                self.Statement.undo_move()
                if score < min_score:
                    min_score = score
                    if depth == self.DEPTH:
                        self.next_move = move
                beta = min(beta, score)
                if alpha >= beta:
                    break
            return min_score

    def isQuiescent(self):
        """
        Function to determine if the current position is 'quiescent'
        """
        for r in range(len(self.Statement.board)):
            for c in range(len(self.Statement.board[r])):
                if self.Statement.board[r][c][0] in ['b', 'r']:
                    return False
        return True
