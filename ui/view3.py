from tkinter import *
from PIL import ImageTk, Image
import pygame as pg
import sys

do_sau = 1

path = "..//VietNamMathChess"
sys.path.append(path)
from game import game


def click_play():
    global do_sau
    do_sau = scale.get()
    view3.destroy()
    g = game.Game()
    while g.running:
        g.new()
    pg.quit()
    sys.exit()


def click_back():
    # view3.withdraw()
    view3.destroy()
    from ui import view2

    # view2.show_view2()


def update_scale():
    text = "ĐỘ SÂU: " + str(scale.get())
    label_scale.config(text=text)
    label_scale.after(15, update_scale)


view3 = Tk()
view3.title("CỜ TOÁN VIỆT NAM")
view3.geometry("600x650+400+30")
view3.resizable(False, False)
view3.iconbitmap("img/logo.ico")
view3.configure(background="#769656")
img = ImageTk.PhotoImage(Image.open("img/bg3.png").resize((600, 650)))
panel = Label(view3, image=img)
panel.place(x=0, y=0, relwidth=1, relheight=1)


bt1 = ImageTk.PhotoImage(Image.open("img/bt3_1.png").resize((250, 70)))
bt2 = ImageTk.PhotoImage(Image.open("img/bt3_2.png").resize((250, 70)))
bt3 = ImageTk.PhotoImage(Image.open("img/bt3_3.png").resize((250, 70)))


scale = Scale(
    view3,
    from_=1,
    to=5,
    bg="#272432",
    fg="#ffffff",
    font=("arial", 20, "bold"),
    border=0,
    orient=HORIZONTAL,
    length=400,
)
scale.place(x=100, y=230)

text = "ĐỘ SÂU: " + str(scale.get())
label_scale = Label(
    view3,
    image=bt3,
    text=text,
    width=10,
    height=2,
    bg="#292d3d",
    fg="#ffffff",
    font=("arial", 20, "bold"),
    border=0,
    compound=CENTER,
)
label_scale.place(x=175, y=330, width=250, height=70)
update_scale()


button_back = Button(
    view3,
    image=bt2,
    border=0,
    bg="#272432",
    command=click_back,
)
button_back.place(x=50, y=500, width=250, height=70)

button_play = Button(
    view3,
    image=bt1,
    border=0,
    bg="#272432",
    command=click_play,
)
button_play.place(x=300, y=500, width=250, height=70)

view3.mainloop()
