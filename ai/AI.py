piece_score = {'0': 100, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 8, '7': 10, '8': 15, '9': 20}

COLUMN = 9
ROW = 11


class AI:
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

    def AI_move(self):
        pass

    def findMove(self, valid_moves):
        pass
