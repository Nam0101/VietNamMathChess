from os import path

import pygame as pg

import state.move as move
import state.state as state

WIDTH = 576
HEIGHT = 704
TITLE = "Cờ Toán Việt Nam"
FPS = 60
FONT_NAME = 'arial'
icon = 'img/logo.jfif'
COLUMN = 9
ROW = 11
SQUARE_SIZE = HEIGHT // ROW
INF = 1000000000
color = [(238, 238, 210), (118, 150, 86)]


def show_start_screen():
    game_folder = path.dirname(__file__)
    img_folder = path.join(game_folder, '../img')
    background = pg.image.load(path.join(img_folder, 'background.png')).convert()
    pass


class Game:

    def __init__(self):
        self.state = state.state()
        # initialize game window,
        self.canvas = None
        self.all_sprites = None
        self.selected_square = (INF, INF)
        self.previous_square = ()
        self.valid_moves = self.state.get_all_possible_move()
        self.player_clicks = []
        self.move_made = False
        self.highlight_color = [(255, 0, 0), (0, 0, 255)]
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_icon(pg.image.load(icon))
        pg.display.set_caption(TITLE)
        self.font_name = pg.font.match_font(FONT_NAME)
        self.clock = pg.time.Clock()
        self.running = True
        self.piece = ["b0", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9",
                      "r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9"]
        self.piece_img = {}
        for i in range(len(self.piece)):
            self.piece_img[self.piece[i]] = pg.image.load("img/" + self.piece[i] + ".png").convert_alpha()
            self.piece_img[self.piece[i]] = pg.transform.scale(self.piece_img[self.piece[i]],
                                                               (SQUARE_SIZE, SQUARE_SIZE))

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.run()

    def run(self):
        # Game Loop
        self.state.playing = True
        while self.state.playing:
            self.clock.tick(FPS)
            self.update()
            self.events()
            self.draw_state()
            pg.display.flip()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.state.playing:
                    self.state.playing = False
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
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
                    movement = move.move(self.player_clicks[0], self.player_clicks[1], self.state.board)
                    self.move_made = True
                    self.state.make_move(movement, self.valid_moves)
                    self.player_clicks = []
                    self.selected_square = ()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_z:
                    self.state.undo_move()
                    self.move_made = True
                if event.key == pg.K_ESCAPE:
                    self.state.playing = False
                    self.running = False
            if self.move_made:
                self.valid_moves = self.state.get_all_possible_move()
                self.move_made = False

    def draw_board(self):
        for i in range(ROW):
            for j in range(COLUMN):
                pg.draw.rect(self.screen, color[(i + j) % 2],
                             pg.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_piece(self):
        for i in range(ROW):
            for j in range(COLUMN):
                piece = self.state.board[i][j]
                if piece != "--":
                    self.screen.blit(self.piece_img[piece],
                                     pg.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_state(self):
        self.draw_board()
        self.draw_piece()
        self.high_light()

    def show_go_screen(self):
        # game over/continue
        pass

    def high_light(self):
        # if self.previous_square is not None: x, y = self.previous_square pg.draw.rect(self.screen, color[(x + y) %
        # 2], (y * SQUARE_SIZE, x * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) if self.selected_square is not None and
        # self.selected_square != (INF, INF): row, col = self.selected_square rect = pg.Rect(col * SQUARE_SIZE,
        # row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE) pg.draw.rect(self.screen, self.highlight_color, rect,
        # 4) self.previous_square = (row, col)
        if self.selected_square != () and self.selected_square != (INF, INF):
            row, col = self.selected_square
            if self.state.board[row][col][0] == ('r' if self.state.red_turn else 'b'):
                pg.draw.rect(self.screen, self.highlight_color[0 if self.state.red_turn else 1],
                             (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 4)
                self.previous_square = (row, col)
                for movement in self.valid_moves:
                    if movement.start_row == row and movement.start_col == col:
                        pg.draw.rect(self.screen, self.highlight_color[0 if self.state.red_turn else 1],
                                     (movement.end_col * SQUARE_SIZE, movement.end_row * SQUARE_SIZE,
                                      SQUARE_SIZE, SQUARE_SIZE), 4)
