
import pygame as pg
import sys
import game.game as game
if __name__ == '__main__':

    g = game.Game()

    # g.show_start_screen()
    while g.running:
        g.new()

        g.show_go_screen()
    pg.quit()
    sys.exit()
