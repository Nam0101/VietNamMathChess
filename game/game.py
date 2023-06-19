import time

import pygame as pg
import time
import state.move as move
import state.state as state
from ai import greedy as greedy, minimax
from numba import jit, njit
import numpy as np
delay = 1
WIDTH = 576
HEIGHT = 704
TITLE = "Cờ Toán Việt Nam"
FPS = 15
FONT_NAME = "arial"
icon = "img/logo.jfif"
COLUMN = 9
ROW = 11
SQUARE_SIZE = HEIGHT // ROW
INF = 1000000000
color = [(238, 238, 210), (118, 150, 86)]

<<<<<<< HEAD
=======
ALGORITHM = {
    0: "Minimax",
    1: "Greedy"
}

>>>>>>> dd1931950123554d01f3af1171dba19c35bae06a

class Game:
    def __init__(self):
        self.state = state.State()
        # initialize game window,
        self.all_sprites = None
        self.selected_square = (INF, INF)
        self.previous_square = ()
        self.valid_moves = self.state.get_all_possible_move()
        self.player_clicks = []
        self.move_made = False
        self.ai_blue = minimax.minimax(3)
        self.ai_red = minimax.minimax(2)
        self.highlight_color = [(254, 0, 0), (0, 0, 254)]
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_icon(pg.image.load(icon))
        pg.display.set_caption(TITLE)
        self.font_name = pg.font.match_font(FONT_NAME)
        self.clock = pg.time.Clock()
        self.running = True
<<<<<<< HEAD
        self.piece = [
            "b0",
            "b1",
            "b2",
            "b3",
            "b4",
            "b5",
            "b6",
            "b7",
            "b8",
            "b9",
            "r0",
            "r1",
            "r2",
            "r3",
            "r4",
            "r5",
            "r6",
            "r7",
            "r8",
            "r9",
        ]
        self.piece_img = {}
        for i in range(len(self.piece)):
            self.piece_img[self.piece[i]] = pg.image.load(
                "img/" + self.piece[i] + ".png"
            ).convert_alpha()
            self.piece_img[self.piece[i]] = pg.transform.scale(
                self.piece_img[self.piece[i]], (SQUARE_SIZE, SQUARE_SIZE)
            )
=======
        self.player_one = True  # if human play red, then this will be true. If AI is playing then this will be false
        self.player_two = False  # same as above
        self.human_turn = True  # if it is human turn, then this will be true
        self.piece = ["b0", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9",
                      "r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9"]
        self.piece_img = {}
        for i in range(len(self.piece)):
            self.piece_img[self.piece[i]] = pg.image.load("img/" + self.piece[i] + ".png").convert_alpha()
            self.piece_img[self.piece[i]] = pg.transform.scale(self.piece_img[self.piece[i]],
                                                               (SQUARE_SIZE, SQUARE_SIZE))
        self.setting(0, 0, True,False)

    def setting(self, dept, algo, player_one, player_two):
        # setting game, dept is dept of game tree, algo is algorithm to use, player_one is true if human play red,
        # false if AI play red, same as player_two
        self.player_one = player_one
        self.player_two = player_two
        self.new()
>>>>>>> dd1931950123554d01f3af1171dba19c35bae06a

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.run()

    def run(self):
        # Game Loop
        while self.running:
            self.clock.tick(FPS)
            self.update()
            self.events()
            self.draw_state()
            pg.display.flip()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        self.human_turn = self.state.red_turn and self.player_one or not self.state.red_turn and self.player_two
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
<<<<<<< HEAD
                x, y = pg.mouse.get_pos()
                row = y // SQUARE_SIZE
                col = x // SQUARE_SIZE
                if self.selected_square == (row, col):
                    self.selected_square = ()
                    self.player_clicks = []
                else:
                    self.selected_square = (row, col)
                    self.player_clicks.append(self.selected_square)
                if len(self.player_clicks) == 2:
                    self.previous_square = self.player_clicks[0]
                    movement = move.Move(
                        self.player_clicks[0], self.player_clicks[1], self.state.board
                    )
                    self.move_made = True
                    self.state.make_move(movement, self.valid_moves)
                    print(self.state.red_score, self.state.blue_score)
                    self.player_clicks = []
                    self.selected_square = ()
=======
                if self.human_turn:
                    x, y = pg.mouse.get_pos()
                    row = y // SQUARE_SIZE
                    col = x // SQUARE_SIZE
                    if self.selected_square == (row, col):
                        self.selected_square = ()
                        self.player_clicks = []
                    else:
                        self.selected_square = (row, col)
                        self.player_clicks.append(self.selected_square)
                    if len(self.player_clicks) == 2:
                        self.previous_square = self.player_clicks[0]
                        movement = move.Move(self.player_clicks[0], self.player_clicks[1], self.state.board)
                        if movement in self.valid_moves:
                            self.state.make_move(movement)
                            print("Human made move", movement.to_string())
                            self.move_made = True
                            print(self.state.red_score, self.state.blue_score)
                            self.player_clicks = []
                            self.selected_square = ()
                        else:
                            self.player_clicks = [self.selected_square]
>>>>>>> dd1931950123554d01f3af1171dba19c35bae06a
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_z:
                    self.state.undo_move()
                    self.state.undo_move()
                    self.move_made = True
                if event.key == pg.K_ESCAPE:
                    self.running = False
            if self.move_made:
                self.valid_moves = self.state.get_all_possible_move()
                self.move_made = False
                self.draw_state()
                if self.state.game_over():
                    print("Game over")
                    self.running = False
            if not self.human_turn and self.running and not self.state.red_turn:
                ai_move = self.ai_blue.findMove(self.state, self.valid_moves)
                self.state.make_move(ai_move)
                self.draw_state()
                self.move_made = True
                print("AI made move", ai_move.to_string())
                self.human_turn = self.state.red_turn and self.player_one or not self.state.red_turn and self.player_two
            if not self.human_turn and self.running and self.state.red_turn:
                ai_move = self.ai_red.findMove(self.state, self.valid_moves)
                self.state.make_move(ai_move)
                self.draw_state()
                self.move_made = True
                self.human_turn = self.state.red_turn and self.player_one or not self.state.red_turn and self.player_two

    def draw_board(self):
        for i in range(ROW):
            for j in range(COLUMN):
                pg.draw.rect(
                    self.screen,
                    color[(i + j) % 2],
                    pg.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )

    def draw_piece(self):
        for i in range(ROW):
            for j in range(COLUMN):
                piece = self.state.board[i][j]
                if piece != "--":
                    self.screen.blit(
                        self.piece_img[piece],
                        pg.Rect(
                            j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE
                        ),
                    )

    def draw_state(self):
        self.draw_board()
        self.draw_piece()
        self.high_light()

    def show_go_screen(self):
        if self.state.game_over():
            print("game over")
            self.running = False
        pass

    def high_light(self):
        if self.selected_square != () and self.selected_square != (INF, INF):
            row, col = self.selected_square
            if self.state.board[row][col][0] == ("r" if self.state.red_turn else "b"):
                pg.draw.rect(
                    self.screen,
                    self.highlight_color[0 if self.state.red_turn else 1],
                    (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                    4,
                )
                self.previous_square = (row, col)
                for movement in (m for m in self.valid_moves):
                    if movement.start_row == row and movement.start_col == col:
                        pg.draw.rect(
                            self.screen,
                            self.highlight_color[0 if self.state.red_turn else 1],
                            (
                                movement.end_col * SQUARE_SIZE,
                                movement.end_row * SQUARE_SIZE,
                                SQUARE_SIZE,
                                SQUARE_SIZE,
                            ),
                            4,
                        )

    def getRedScore(self):
        return self.state.red_score

    def getBlueScore(self):
        return self.state.blue_score
