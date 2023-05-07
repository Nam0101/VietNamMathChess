import pygame as pg
import sys
from os import path

WIDTH = 675
HEIGHT = 825
TITLE = "Cờ Toán Việt Nam"
FPS = 60
FONT_NAME = 'arial'
icon = 'img/logo.jfif'
COLUMN = 9
ROW = 11
SQUARE_SIZE = 75

WHITE = (238, 238, 210)
BLACK = (118, 150, 86)


class Game:
    def __init__(self):
        # initialize game window, etc
        self.playing = None
        self.all_sprites = None
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_icon(pg.image.load(icon))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        # self.broad = [["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9"],
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
        self.board = [["b9", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r1"],
                      ["b8", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r2"],
                      ["b7", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r3"],
                      ["b6", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r4"],
                      ["b5", "b0", "--", "--", "--", "--", "--", "--", "--", "r0", "r5"],
                      ["b4", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r6"],
                      ["b3", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r7"],
                      ["b2", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r8"],
                      ["b1", "--", "--", "--", "--", "--", "--", "--", "--", "--", "r9"]]


        self.piece = ["b0", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9",
                      "r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9"]
        self.piece_img = {}
        for i in range(len(self.piece)):
            self.piece_img[self.piece[i]] = pg.image.load("img/" + self.piece[i] + ".png").convert_alpha()
            self.piece_img[self.piece[i]] = pg.transform.scale(self.piece_img[self.piece[i]], (75, 75))

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
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw_board(self):
        for i in range(COLUMN):
            for j in range(ROW):
                if (i + j) % 2 == 0:
                    pg.draw.rect(self.screen, WHITE, (i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pg.draw.rect(self.screen, BLACK, (i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_piece(self):
        for i in range(COLUMN):
            for j in range(ROW):
                piece = self.board[i][j]
                if piece != "--":
                    self.screen.blit(self.piece_img[piece],
                                     pg.Rect(i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_state(self):
        self.draw_board()
        self.draw_piece()
        pg.display.flip()

    def show_start_screen(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        background = pg.image.load(path.join(img_folder, 'background.png')).convert()
        pass

    def show_go_screen(self):
        # game over/continue
        pass
