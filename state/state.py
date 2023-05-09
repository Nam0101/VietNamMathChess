from state.move import move

COlUMN = 9
ROW = 11

move_direction = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]


class state():
    def __init__(self):
        self.board = [["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9"],
                      ["--", "--", "--", "--", "b0", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "r0", "--", "--", "--", "--"],
                      ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9"]]
        self.playing = False
        self.have_ai = False
        self.red_turn = True
        self.red_score = 0
        self.blue_score = 0
        self.move_log = []

    def check_end(self):
        if self.board[4][2] == "--" or self.board[4][8] == "--":
            self.playing = False
            return False
        return True

    def update_board(self, startCol, startRow, endCol, endRow):
        self.board[endRow][endCol] = self.board[startRow][startCol]
        self.board[startRow][startCol] = "--"
        self.red_turn = not self.red_turn

    def is_playing(self):
        return self.playing

    def make_move(self, move):
        self.update_board(move.startCol, move.startRow, move.endCol, move.endRow)
        self.move_log.append(move)
        self.check_end()
        print(self.move_log.__len__())
        self.red_turn = not self.red_turn

    def undo_move(self):
        if self.move_log.__len__() != 0:
            move = self.move_log.pop()
            self.update_board(move.endCol, move.endRow, move.startCol, move.startRow)
            self.red_turn = not self.red_turn
            self.check_end()
            return move
        return None

    def get_all_possible_move(self):
        moves = []
        for row in range(ROW):
            for col in range(COlUMN):
                turn = self.board[row][col][0]
                if (turn == "r" and self.red_turn) or (turn == "b" and not self.red_turn):
                    piece_step = int(self.board[row][col][1])
                    if piece_step == 0:
                        continue
                    self.get_move_for_piece(piece_step, row, col, moves)

        return moves

    def get_move_for_piece(self, piece_step, row, col, moves):
        for direction in move_direction:
            for i in range(1, piece_step + 1):
                endRow = row + direction[0] * i
                endCol = col + direction[1] * i
                if endRow < 0 or endRow >= ROW or endCol < 0 or endCol >= COlUMN:
                    break
                endPiece = self.board[endRow][endCol]
                if endPiece == "--":
                    moves.append(move((row, col), (endRow, endCol), self.board))
                else:
                    if endPiece[0] == "r" and self.red_turn:
                        break
                    elif endPiece[0] == "b" and not self.red_turn:
                        break
                    else:
                        moves.append(move((row, col), (endRow, endCol), self.board))
                        break
