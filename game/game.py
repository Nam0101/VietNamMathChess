from os import path

import pygame
import pygame as pg

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
        # initialize game window,
        self.canvas = None
        self.all_sprites = None
        self.selected_square = None
        self.previous_square = None
        self.highlight_color = (255, 255, 0)
        self.state = state.state()
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_icon(pg.image.load(icon))
        pg.display.set_caption(TITLE)
        self.font_name = pg.font.match_font(FONT_NAME)
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
            self.get_piece_clicked()
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
                return INF, INF
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // SQUARE_SIZE
                col = x // SQUARE_SIZE
                return row, col
        return INF, INF

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
        self.high_light()
        self.draw_piece()


    def show_go_screen(self):
        # game over/continue
        pass

    def get_piece_clicked(self):
        event_result = self.events()
        if event_result is not None:
            x, y = event_result
            self.selected_square = (x, y)
            if x == INF and y == INF:
                return None
            piece = self.state.board[x][y]
            if piece != "--":
                print("Vị trí: ", x, y)
                print(piece)
                return piece

    def high_light(self):

        if self.previous_square is not None:
            x, y = self.previous_square
            pg.draw.rect(self.screen, color[(x + y) % 2], (y * SQUARE_SIZE, x * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        if self.selected_square is not None and self.selected_square != (INF, INF):
            row, col = self.selected_square
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(self.screen, self.highlight_color, rect, 4)
            self.previous_square = (row, col)





