import pygame as pg
import sys
from os import path

WIDTH = 675
HEIGHT = 825
TITLE = "Cờ Toán Việt Nam"
FPS = 60
FONT_NAME = 'arial'
icon = 'img/logo.jfif'
COLUMN = 11
ROW = 9
SQUARE_SIZE = 75

WHITE = (238,238,210)
BLACK = (118,150,86)


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
            self.draw_broad()

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

    def draw_broad(self):
        for i in range(ROW):
            for j in range(COLUMN):
                if (i + j) % 2 == 0:
                    pg.draw.rect(self.screen, WHITE, (i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pg.draw.rect(self.screen, BLACK, (i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        pg.display.flip()

    def show_start_screen(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        background = pg.image.load(path.join(img_folder, 'background.png')).convert()
        pass

    def show_go_screen(self):
        # game over/continue
        pass


