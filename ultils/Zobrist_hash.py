import random

import numpy as np


class zobrist_hash:
    def __init__(self):
        self.NUM_PIECES = 20
        self.ROWS = 11
        self.COLS = 9
        self.zobrist_keys = np.zeros((self.ROWS, self.COLS, self.NUM_PIECES), dtype=np.uint64)
        self.initKeys()

    def initKeys(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                for piece in range(self.NUM_PIECES):
                    self.zobrist_keys[row, col, piece] = random.getrandbits(64)

    def calculate_zobrist_hash(self, board):
        hash_value = np.uint64(0)
        rows, cols = np.where(board != "--")
        for row, col in zip(rows, cols):
            piece = board[row, col]
            piece_index = int(piece[1])
            if piece[0] == "r":
                piece_index += 10
            hash_value ^= self.zobrist_keys[row, col, piece_index]
        return hash_value