from game.game import Game
if __name__ == "__main__":
    # from ui import view1

    # view1.mainloop()
    game = Game(3, 1, 1, True, False)
    while game.running:
        game.new()
