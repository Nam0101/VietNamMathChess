import sys

import pygame as pg
import game.game as game
if __name__ == '__main__':
    g = game.Game()

    while g.running:
        g.new()
    pg.quit()
    sys.exit()
