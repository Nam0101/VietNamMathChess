import sys

import numpy as np
import pygame as pg

import state.move as move
import state.state as state
from ai import minimax
from ai.greedy import greedy
from ai.negamax import Negamax
from ai.negascout import NegaScout

delay = 1
WIDTH = 704
HEIGHT = 704
sub_screen_height = HEIGHT
sub_screen_width = HEIGHT - 576
TITLE = "Cờ Toán Việt Nam"
FPS = 15
FONT_NAME = "timesnewroman"
icon = "img/logo.jfif"
COLUMN = 9
ROW = 11
SQUARE_SIZE = HEIGHT // ROW
INF = 1000000000
color = [(238, 238, 210), (118, 150, 86)]

ALGORITHM = {0: "Minimax", 1: "Greedy"}


# cài đặt ở hàm init game.
# args:
# dept1: độ sâu cho AI Red
# dept2: độ sâu cho AI Blue
# algo1: thuật toán cho AI1, int
# algo2: thuật toán cho AI2, int
# player_one: người chơi 1, bool, nếu người chơi 1 là người thì True, nếu là AI thì False
# player_two: người chơi 2, bool, nếu người chơi 2 là người thì True, nếu là AI thì False
# ví dụ: game = Game(2,2, 2, False, False) -> người chơi 1 là AI, người chơi 2 là AI, độ sâu là 2, thuật toán 1 là Minimax, thuật toán 2 là Minimax
# 1-> greedy
# 2-> AlphaBeta
# 3 -> Negamax
# 4 -> NegaScout

class Game:

    def __init__(self, dept1, dept2, algo1, algo2, player_one, player_two):
        self.state = state.State()
        # initialize game window,
        self.all_sprites = None
        self.selected_square = (INF, INF)
        self.previous_square = ()
        self.valid_moves = self.state.get_all_valid_move()
        self.player_clicks = []
        self.ai_red = None
        self.ai_blue = None
        self.move_made = False
        if not player_one:
            if algo1 == 1:
                self.ai_red = greedy()
            elif algo1 == 2:
                self.ai_red = minimax.minimax(dept1)
            elif algo1 == 3:
                self.ai_red = Negamax(dept1)
            elif algo1 == 4:
                self.ai_red = NegaScout(dept1)
        if not player_two:
            if algo2 == 1:
                self.ai_blue = greedy()
            elif algo2 == 2:
                self.ai_blue = minimax.minimax(dept2)
            elif algo2 == 3:
                self.ai_blue = Negamax(dept2)
            elif algo2 == 4:
                self.ai_blue = NegaScout(dept2)
        self.highlight_color = [(230, 0, 0), (0, 0, 230)]
        pg.init()
        self.sub_screen = pg.Surface((sub_screen_width, sub_screen_height))
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_icon(pg.image.load(icon))
        pg.display.set_caption(TITLE)
        self.font_name = pg.font.match_font(FONT_NAME)
        self.clock = pg.time.Clock()
        self.running = True
        self.player_one = player_one  # if human play red, then this will be true. If AI is playing then this will be false
        self.player_two = player_two  # same as above
        self.human_turn = True  # if it is human turn, then this will be true
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
            self.piece_img[self.piece[i]] = pg.image.load("img/" + self.piece[i] + ".png").convert_alpha()
            self.piece_img[self.piece[i]] = pg.transform.scale(self.piece_img[self.piece[i]],
                                                               (SQUARE_SIZE, SQUARE_SIZE))
            self.piece_img[self.piece[i]] = pg.image.load(
                "img/" + self.piece[i] + ".png"
            ).convert_alpha()
            self.piece_img[self.piece[i]] = pg.transform.scale(
                self.piece_img[self.piece[i]], (SQUARE_SIZE, SQUARE_SIZE)
            )

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.run()

    def run(self):
        # Game Loop
        while self.running:
            self.update()
            self.draw_state()
            self.events()
            self.draw_state()
            pg.display.flip()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        self.human_turn = (
                self.state.red_turn
                and self.player_one
                or not self.state.red_turn
                and self.player_two
        )
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.human_turn:
                    x, y = pg.mouse.get_pos()
                    row = y // SQUARE_SIZE
                    col = x // SQUARE_SIZE
                    if 0 <= row < ROW and 0 <= col < COLUMN:
                        if self.selected_square == (row, col):
                            self.selected_square = ()
                            self.player_clicks = []
                        else:
                            self.selected_square = (row, col)
                            self.player_clicks.append(self.selected_square)
                        if len(self.player_clicks) == 2:
                            self.previous_square = self.player_clicks[0]
                            movement = move.Move(
                                self.player_clicks[0],
                                self.player_clicks[1],
                                self.state.board,
                            )
                            if movement in self.valid_moves:
                                self.state.make_move(movement)
                                print("Human made move", movement.to_string())
                                self.move_made = True
                                self.player_clicks = []
                                self.selected_square = ()
                            else:
                                self.player_clicks = [self.selected_square]
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_z:
                    self.state.undo_move()
                    if not self.player_one or not self.player_two:
                        self.state.undo_move()
                    self.move_made = True
                if event.key == pg.K_ESCAPE:
                    self.running = False
                    pg.display.quit()
                    pg.quit()
                    sys.exit()
        if self.move_made:
            self.valid_moves = self.state.get_all_valid_move()
            self.move_made = False
            self.draw_state()
        if self.state.game_over() == 1 or self.state.game_over() == 2:
            from ui.results import Results
            kq = Results(
                self.state.red_score,
                self.state.blue_score,
                self.state.game_over(),
            )
            pg.display.quit()
            pg.quit()
            kq.show_results()
            print("Game over")
            self.running = False
        if not self.human_turn and self.running and not self.state.red_turn:
            self.draw_state()
            ai_move = self.ai_blue.AI_find_move(self.state, self.valid_moves)
            self.state.make_move(ai_move)
            self.draw_state()
            self.move_made = True
            print("AI made move", ai_move.to_string())
            self.human_turn = (
                    self.state.red_turn
                    and self.player_one
                    or not self.state.red_turn
                    and self.player_two
            )
        if not self.human_turn and self.running and self.state.red_turn:
            self.draw_state()
            ai_move = self.ai_red.AI_find_move(self.state, self.valid_moves)
            self.state.make_move(ai_move)
            self.draw_state()
            print("AI made move", ai_move.to_string())
            self.move_made = True
            self.human_turn = (
                    self.state.red_turn
                    and self.player_one
                    or not self.state.red_turn
                    and self.player_two
            )

    def draw_board(self):
        for i in range(ROW):
            for j in range(COLUMN):
                pg.draw.rect(
                    self.screen,
                    color[(i + j) % 2],
                    pg.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )

    def draw_piece(self):
        rows, cols = np.where(self.state.board != "--")
        for i, j in zip(rows, cols):
            piece = self.state.board[i][j]
            self.screen.blit(
                self.piece_img[piece], pg.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), )

    def draw_state(self):
        self.draw_board()
        self.draw_piece()
        self.high_light()
        self.draw_scores()
        self.screen.blit(self.sub_screen, (WIDTH - sub_screen_width, 0))

    def draw_scores(self):
        self.sub_screen.fill((250, 235, 215))
        score_section_height = sub_screen_height // 2
        score_section_width = sub_screen_width
        font = pg.font.Font(self.font_name, 60)
        blue_score_text = font.render(str(self.state.blue_score), True, (0, 0, 255))
        blue_score_rect = blue_score_text.get_rect()
        blue_score_rect.center = (score_section_width // 2, score_section_height // 2)
        self.sub_screen.blit(blue_score_text, blue_score_rect)
        red_score_text = font.render(str(self.state.red_score), True, (255, 0, 0))
        red_score_rect = red_score_text.get_rect()
        red_score_rect.center = (score_section_width // 2, score_section_height + score_section_height // 2)
        self.sub_screen.blit(red_score_text, red_score_rect)

    def show_go_screen(self):
        if self.state.game_over() == 1 or self.state.game_over() == 2:
            from ui.results import Results
            kq = Results(
                self.state.red_score,
                self.state.blue_score,
                self.state.game_over(),
            )
            kq.show_results()
            pg.display.quit()
            pg.quit()
            print("game over")
            self.running = False


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
                        pg.draw.rect(self.screen, self.highlight_color[0 if self.state.red_turn else 1],
                                     (movement.end_col * SQUARE_SIZE, movement.end_row * SQUARE_SIZE,
                                      SQUARE_SIZE, SQUARE_SIZE), 4)
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
