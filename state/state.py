from .move import move

COlUMN = 9
ROW = 11

move_direction = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]


class state:
    def __init__(self):
        self.board = [["b9", "b8", "b7", "b6", "b5", "b4", "b3", "b2", "b1"],
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

    def update_board(self, movement):
        self.board[movement.start_row][movement.start_col] = "--"
        self.board[movement.end_row][movement.end_col] = movement.piece_moved


    def is_playing(self):
        return self.playing

    def make_move(self, movement, valid_moves):
        if self.red_turn and self.board[movement.start_row][movement.start_col][0] == "b":
            return
        if not self.red_turn and self.board[movement.start_row][movement.start_col][0] == "r":
            return
        if self.board[movement.end_row][movement.end_col][0] == self.board[movement.start_row][movement.start_col][0]:
            return
        if self.board[movement.start_row][movement.start_col] == "--":
            return
        for valid_move in valid_moves:
            if movement == valid_move:
                self.update_board(movement)
                self.move_log.append(movement)
                self.red_turn = not self.red_turn

    def undo_move(self):
        if self.move_log.__len__() != 0:
            movement = self.move_log.pop()
            self.update_board(movement.endCol, movement.endRow, movement.startCol, movement.startRow)
            self.red_turn = not self.red_turn

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
                    self.attack_move(piece_step, turn, row, col, moves)
        return moves

    def get_move_for_piece(self, piece_step, row, col, moves):
        for direction in move_direction:
            for i in range(1, piece_step + 1):
                end_row = row + direction[0] * i
                end_col = col + direction[1] * i
                if end_row < 0 or end_row >= ROW or end_col < 0 or end_col >= COlUMN:
                    break
                end_piece = self.board[end_row][end_col]
                if end_piece == "--":
                    moves.append(move((row, col), (end_row, end_col), self.board))
                else:
                    break

    def attack_move(self, piece_step, piece_color, row, col, moves):
        for i, j in move_direction:
            if 0 <= row + i < ROW and 0 <= col + j < COlUMN:
                color = self.board[row + i][col + j][0]
                if color == piece_color:
                    team_piece = int(self.board[row + i][col + j][1])
                    if team_piece == 0:
                        continue
                    add_attack = piece_step + team_piece
                    sub_attack = piece_step - team_piece
                    multi_attack = piece_step * team_piece
                    division_attack = piece_step // team_piece
                    remain_attack = piece_step % team_piece
                    attack_step = [add_attack, sub_attack, multi_attack, division_attack, remain_attack]
                    self.get_attack_move(attack_step, (row, col), (i, j), moves)

    def get_attack_move(self, attack_step, current_piece, direction, moves):
        enemy_color = "b" if self.red_turn else "r"
        row, col = current_piece
        i, j = direction
        row, col = (row + i), (col + j)
        for step in attack_step:
            if step <= 0:
                continue
            step %= 10
            can_attack = True
            for x in range(1, step):
                end_row = row + i * x
                end_col = col + j * x
                if 0 <= end_row < ROW and 0 <= end_col < COlUMN:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "--":
                        continue
                    else:
                        can_attack = False
                        break
                else:
                    can_attack = False
                    break
            if can_attack:
                end_row = row + i * step
                end_col = col + j * step
                if 0 <= end_row < 11 and 0 <= end_col < 9:
                    end_piece = self.board[end_row][end_col]
                    if end_piece[0] == enemy_color:
                        moves.append(move(current_piece, (end_row, end_col), self.board))
