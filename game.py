import pygame as pg
import sys
from os import path
import GameState.State as State

WIDTH = 576
HEIGHT = 704
TITLE = "Cờ Toán Việt Nam"
FPS = 60
FONT_NAME = 'arial'
icon = 'img/logo.jfif'
COLUMN = 9
ROW = 11
SQUARE_SIZE = HEIGHT//ROW


color = [(238, 238, 210), (118, 150, 86)]


def show_start_screen():
    game_folder = path.dirname(__file__)
    img_folder = path.join(game_folder, 'img')
    background = pg.image.load(path.join(img_folder, 'background.png')).convert()
    pass


class Game:

    def __init__(self):
        # initialize game window,
        self.state = State.state()
        self.playing = None
        self.all_sprites = None
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_icon(pg.image.load(icon))
        pg.display.set_caption(TITLE)
        # xoay màn hình 90 độ
        # self.screen = pg.transform.rotate(self.screen, 90)
        # self.screen = pg.transform.flip(self.screen, True, False)
        self.clock = pg.time.Clock()
        self.running = True
        # self.board = [["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9"],
        #               ["--", "--", "--", "--", "r0", "--", "--", "--", "--"],
        #               ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
        #               ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
        #               ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
        #               ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
        #               ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
        #               ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
        #               ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
        #               ["--", "--", "--", "--", "r0", "--", "--", "--", "--"],
        #               ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9"]]

        self.piece = ["b0", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9",
                      "r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9"]
        self.piece_img = {}
        for i in range(len(self.piece)):
            self.piece_img[self.piece[i]] = pg.image.load("img/" + self.piece[i] + ".png").convert_alpha()
            self.piece_img[self.piece[i]] = pg.transform.scale(self.piece_img[self.piece[i]], (SQUARE_SIZE, SQUARE_SIZE))

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw_state()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

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
        pg.display.flip()

    def show_go_screen(self):
        # game over/continue
        pass

    # return piece is clicked on
    def get_piece(self, x, y):
        if x < 0 or x > 8 or y < 0 or y > 10:
            return "--"
        return self.state.board[x][y]
