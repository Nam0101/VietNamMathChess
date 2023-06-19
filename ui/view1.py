from tkinter import *
from PIL import ImageTk, Image
import pygame as pg
import sys

path = "..//VietNamMathChess"
sys.path.append(path)
from game import game


# x = 3


def show_view1():
    view1.deiconify()


def click_nguoi_nguoi():
    # global x
    # x = 1
    # button_nguoi_nguoi.config(bg="#0812aa")
    # button_nguoi_may.config(bg="#595fae")
    # button_may_may.config(bg="#595fae")
    view1.withdraw()
    g = game.Game()
from game.game import Game


def click_man_man():
    view1.destroy()
    g = Game()
    while g.running:
        g.new()
    pg.quit()
    sys.exit()


def click_view2():
    view1.destroy()
    from ui import view2


def click_instruct():
    from ui.instruct import show_instruct

    show_instruct()


view1 = Tk()
view1.title(" CỜ TOÁN VIỆT NAM")
view1.geometry("600x650+400+30")
view1.resizable(False, False)
view1.iconbitmap("img/logo.ico")
img = ImageTk.PhotoImage(Image.open("img/bg1.png").resize((600, 650)))
panel = Label(view1, image=img)
panel.place(x=0, y=0, relwidth=1, relheight=1)

bt1 = ImageTk.PhotoImage(Image.open("img/bt1.png").resize((300, 80)))
bt2 = ImageTk.PhotoImage(Image.open("img/bt2.png").resize((300, 80)))
bt3 = ImageTk.PhotoImage(Image.open("img/bt3.png").resize((300, 80)))
bt4 = ImageTk.PhotoImage(Image.open("img/bt4.png").resize((300, 80)))


botton_man_man = Button(
    view1,
    image=bt1,
    bg="#062336",
    border=0,
    command=click_man_man,
)
botton_man_man.place(x=150, y=150, width=300, height=80)

button_man_bot = Button(
    view1,
    image=bt2,
    bg="#062336",
    border=0,
    command=click_view2,
)
button_man_bot.place(x=150, y=250, width=300, height=80)

button_bot_bot = Button(
    view1,
    image=bt3,
    bg="#062336",
    border=0,
    command=click_view2,
)
button_bot_bot.place(x=150, y=350, width=300, height=80)

button_instruct = Button(
    view1,
    image=bt4,
    bg="#062336",
    border=0,
    command=click_instruct,
)
button_instruct.place(x=153, y=480, width=300, height=80)

view1.mainloop()
