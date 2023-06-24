import tkinter as tk

from game.game import Game

if __name__ == "__main__":
    player_one = True
    player_two = True
    algo1 = 0
    algo2 = 0
    dept1 = 0
    dept2 = 0
    # game = Game(0,2, 2, 2, True, False)
    # while game.running:
    #     game.new()
    while True:
        from ui import view1
        if(view1.player_one == True and view1.player_two == True):
            game = Game(0,0, 0, 0, True, True)
            while game.running:
                game.new()
            break
        elif(view1.player_one == True and view1.player_two == False):
            from ui import view2
            if(view2.algo == -1):
                continue
            else:
                if(view2.algo == 1):
                    game = Game(0,0, 1, 1, True, False)
                    while game.running:
                        game.new()
                    break
                else:
                    from ui import view3
                    if(view3.dept == -1):
                        continue
                    else:
                        game = Game(0,view3.dept, 2, 2, True, False)
                        while game.running:
                            game.new()
                        break
        elif(view1.player_one == False and view1.player_two == False):
            from ui import view2
            if(view2.algo == -1):
                continue
            else:
                algo1 = view2.algo
                from ui import view2
                if(view2.algo == -1):
                    continue
                else:
                    algo2 = view2.algo

                if(algo1 == 1 and algo2 == 1):
                    game = Game(0,0, 1, 1, False, False)
                    while game.running:
                        game.new()
                    break
                elif(algo1 == 1 or algo2 == 1):
                    from ui import view3
                    if(view3.dept == -1):
                        continue
                    else:
                        if(algo1 == 1):
                            game = Game(0,view3.dept, 1,algo2, False, False)
                            while game.running:
                                game.new()
                            break
                        else:
                            game = Game(0,view3.dept, algo1, 1, False, False)
                            while game.running:
                                game.new()
                            break
                else:
                    from ui import view4
                    if(view4.dept1 == -1 and view4.dept2 == -1):
                        continue
                    else:
                        game = Game(view4.dept1,view4.dept2, algo1, algo2, False, False)
                        while game.running:
                            game.new()
                        break
