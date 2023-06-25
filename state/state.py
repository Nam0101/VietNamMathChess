import numpy as np

from .move import Move

COlUMN = 9
ROW = 11

move_direction = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]


class State:
    def __init__(self):
        self.board = np.array(
            [
                ["b9", "b8", "b7", "b6", "b5", "b4", "b3", "b2", "b1"],
                ["--", "--", "--", "--", "b0", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                ["--", "--", "--", "--", "r0", "--", "--", "--", "--"],
                ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9"],
            ],
            dtype=np.str_,
        )
        self.red_turn = True
        self.red_score = 0
        self.blue_score = 0
        self.move_log = []

    def make_move(self, movement):
        self.board[movement.start_row, movement.start_col] = "--"
        self.board[movement.end_row, movement.end_col] = movement.piece_moved
        self.calculate_score()
        self.move_log.append(movement)
        self.red_turn = not self.red_turn

    def undo_move(self):
        if self.move_log.__len__() != 0:
            movement = self.move_log.pop()
            self.board[movement.start_row, movement.start_col] = movement.piece_moved
            self.board[movement.end_row, movement.end_col] = movement.piece_captured
            self.calculate_score()
            self.red_turn = not self.red_turn

    def game_over(self):
        if self.red_score >= 25 or self.board[1, 4] != "b0":
            return 1
        if self.blue_score >= 25 or self.board[9, 4] != "r0":
            return 2

    def last_move(self):
        if self.move_log.__len__() != 0:
            return self.move_log[-1]
        return None

    def calculate_score(self):
        self.red_score = 45
        self.blue_score = 45
        row, col = np.where(self.board != "--")
        for r, c in zip(row, col):
            piece = self.board[r, c]
            score = int(piece[1])
            if piece[0] == "r":
                self.blue_score -= score
            else:
                self.red_score -= score
        return self.red_score, self.blue_score

    def get_all_attack_move(self):
        moves = self.get_all_valid_move()
        attack_moves = filter(lambda move: move.is_attack, moves)
        return attack_moves

    def get_all_valid_move(self):
        moves = []
        rows, cols = np.where(self.board != "--")
        for row, col in zip(rows, cols):
            piece = self.board[row, col]
            turn = piece[0]
            if (turn == "r" and self.red_turn) or (turn == "b" and not self.red_turn):
                piece_step = int(self.board[row, col][1])
                if piece_step == 0:
                    continue
                moves.extend(self.attack_move(piece_step, turn, row, col))
                moves.extend(self.get_move_for_piece(piece_step, row, col))
        return moves

    def get_move_for_piece(self, piece_step, row, col):
        possible_moves = []
        for direction in move_direction:
            for i in range(1, piece_step + 1):
                end_row = row + direction[0] * i
                end_col = col + direction[1] * i
                if end_row < 0 or end_row >= ROW or end_col < 0 or end_col >= COlUMN:
                    break
                end_piece = self.board[end_row, end_col]
                if end_piece == "--":
                    possible_moves.append(
                        Move((row, col), (end_row, end_col), self.board)
                    )
                else:
                    break
        return possible_moves

    def attack_move(self, piece_step, piece_color, row, col):
        possible_moves = []
        for i, j in move_direction:
            if 0 <= row + i < ROW and 0 <= col + j < COlUMN:
                color = self.board[row + i, col + j][0]
                if color == piece_color:
                    team_piece = int(self.board[row + i, col + j][1])
                    if team_piece == 0:
                        continue
                    add_attack = piece_step + team_piece
                    sub_attack = piece_step - team_piece
                    multi_attack = piece_step * team_piece
                    division_attack = piece_step // team_piece
                    remain_attack = piece_step % team_piece
                    if piece_step < team_piece:
                        division_attack = 0
                        remain_attack = 0
                    attack_step = [
                        add_attack,
                        sub_attack,
                        multi_attack,
                        division_attack,
                        remain_attack,
                    ]
                    possible_moves.extend(
                        self.get_attack_move(attack_step, (row, col), (i, j))
                    )
        return possible_moves

    def get_attack_move(self, attack_step, current_piece, direction):
        enemy_color = "b" if self.red_turn else "r"
        row, col = current_piece
        i, j = direction
        row, col = (row + i), (col + j)
        possible_moves = []
        for step in attack_step:
            if step <= 0:
                continue
            step %= 10
            can_attack = True
            for x in range(1, step):
                end_row = row + i * x
                end_col = col + j * x
                if 0 <= end_row < ROW and 0 <= end_col < COlUMN:
                    end_piece = self.board[end_row, end_col]
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
                if 0 <= end_row < ROW and 0 <= end_col < COlUMN:
                    end_piece = self.board[end_row, end_col]
                    if end_piece[0] == enemy_color:
                        possible_moves.append(Move(current_piece, (end_row, end_col), self.board))
        return possible_moves

    def to_string(self):
        s = self.board.__str__()
        s += "turn: " + self.red_turn.__str__() + "\n"
        return s

    def is_check(self):
        king_row = 1 if self.red_turn else 9
        king_col = 4
        for move in self.get_all_valid_move():
            if move.end_row == king_row and move.end_col == king_col:
                return True
        return False
