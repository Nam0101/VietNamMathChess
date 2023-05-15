import sys
import ui.view1 as view1
import pygame as pg
import game.game as game
if __name__ == '__main__':
    view1.mainloop()
    g = game.Game()

    while g.running:
        g.new()
    pg.quit()
    sys.exit()
