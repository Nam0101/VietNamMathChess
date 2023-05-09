import sys

import pygame as pg

import game.game as game

if __name__ == '__main__':

    g = game.Game()

    # g.show_start_screen()
    while g.running:
        g.new()
    pg.quit()
    sys.exit()
