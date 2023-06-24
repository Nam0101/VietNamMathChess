import tkinter as tk

from game.game import Game

if __name__ == "__main__":
    # from ui import view1
    #
    # view1 = tk.Tk()
    #
    # view1.mainloop()
    # dept1,dept2, algo1, algo2, player_one, player_two
    game = Game(3, 2, 2, 2, True, False)
    while game.running:
        game.new()
