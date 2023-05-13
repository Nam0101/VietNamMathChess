import state.state as state

piece_score = {'0': 100, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 8, '7': 10, '8': 15, '9': 20}

COLUMN = 9
ROW = 11


class StateEvaluation:
    state = state.State()

    def evaluation(self):
        board = self.state.board
        score = 0
        for row in range(ROW):
            for col in range(COLUMN):
                piece = board[row][col]
                if piece != "--":
                    if piece[0] == 'r':
                        score += piece_score[piece[1]]
                    else:
                        score -= piece_score[piece[1]]

        return score
