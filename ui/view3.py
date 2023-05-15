from tkinter import *
from PIL import ImageTk, Image
import pygame as pg
import sys

do_sau = 1

path = "..//VietNamMathChess"
sys.path.append(path)
from game import game


def show_view3():
    view3.deiconify()


def click_play():
    global do_sau
    do_sau = scale.get()
    view3.withdraw()
    g = game.Game()
    while g.running:
        g.new()
    pg.quit()
    sys.exit()


def click_back():
    view3.withdraw()
    from ui import view2

    view2.show_view2()


def update_scale():
    label_scale2.config(text=scale.get())
    label_scale2.after(15, update_scale)


view3 = Tk()
view3.title("CỜ TOÁN VIỆT NAM")
view3.geometry("600x600+400+50")
view3.resizable(False, False)
view3.iconbitmap("img/logo.ico")
view3.configure(background="#769656")
# img = Image.open("img/bg6.png")
# # img = img.resize((600, 600), Image.ANTIALIAS)
# img = ImageTk.PhotoImage(img)
# panel = Label(view3, image=img)
# # panel.image = img
# panel.place(x=0, y=0, relwidth=1, relheight=1)

label_title = Label(
    view3,
    text="CHỌN ĐỘ SÂU",
    bg="#769656",
    fg="#8cfffb",
    font=("monaco", 35, "bold"),
)
label_title.place(x=140, y=100)

scale = Scale(
    view3,
    from_=1,
    to=5,
    bg="#8cfffb",
    fg="#000000",
    orient=HORIZONTAL,
    length=400,
)
scale.place(x=100, y=200)

label_scale1 = Label(
    view3,
    text="ĐỘ SÂU: ",
    width=10,
    height=2,
    bg="#8cfffb",
    fg="#000000",
    font=("arial", 20, "bold"),
)
label_scale1.place(x=200, y=300)

label_scale2 = Label(
    view3,
    text=scale.get(),
    width=5,
    height=2,
    bg="#8cfffb",
    fg="#000000",
    font=("arial", 20, "bold"),
)
label_scale2.place(x=330, y=300)
update_scale()


button_back = Button(
    view3,
    text="QUAY LẠI",
    width=10,
    height=1,
    bg="#b97a56",
    fg="#ffffff",
    font=("arial", 18, "bold"),
    command=click_back,
)
button_back.place(x=90, y=450)

button_play = Button(
    view3,
    text="PLAY",
    width=10,
    height=1,
    bg="#0ed145",
    fg="#ffffff",
    font=("arial", 18, "bold"),
    command=click_play,
)
button_play.place(x=350, y=450)

view3.mainloop()
