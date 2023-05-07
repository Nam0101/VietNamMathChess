COlUMN = 9
ROW = 11

dX = [0, 1, 0, -1, 1, 1, -1, -1]
dY = [-1, 0, 1, 0, -1, 1, 1, -1]


class state():
    def __init__(self):
        # self.board = [["b9", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r1"],
        #               ["b8", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r2"],
        #               ["b7", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r3"],
        #               ["b6", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r4"],
        #               ["b5", "b0", "--", "--", "--", "--", "--", "--", "--", "r0", "r5"],
        #               ["b4", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r6"],
        #               ["b3", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r7"],
        #               ["b2", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r8"],
        #               ["b1", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r9"]]
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
        self.is_end = False
        self.AI_turn = False
        self.AI_score = 0
        self.player_score = 0
        self.AI_side = "b"
        self.player_side = "r"

    def check_end(self):
        if self.board[4][2] == "--" or self.board[4][8] == "--":
            self.is_end = True
            return True
        return False

    def check_win(self):
        if self.AI_score >= 30 or self.player_score >= 30:
            self.is_end = True
            return True
        return False
