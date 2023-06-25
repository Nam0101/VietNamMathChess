import tkinter as tk

# import sys
# import pygame as pg
from PIL import ImageTk, Image

# path = "..//VietNamMathChess"
# sys.path.append(path)
# from game import game

player_one = True
player_two = True

def click_man_man(event):
    global player_one, player_two
    player_one = True
    player_two = True
    view1.destroy()

def click_man_bot(event):
    global player_one, player_two
    player_one = True
    player_two = False
    view1.destroy()

def click_bot_bot(event):
    global player_one, player_two
    player_one = False
    player_two = False
    view1.destroy()

def click_instruct(event):
    pass

view1 = tk.Tk()
view1.title(" CỜ TOÁN VIỆT NAM")
view1.geometry("550x650+400+30")
view1.resizable(False, False)
view1.iconbitmap("img/logo.ico")

canvas = tk.Canvas(view1, width=700, height=750)
canvas.place(x=-2, y=-1)

img = ImageTk.PhotoImage(Image.open("img/bg1.png").resize((552, 652)))
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)


bt1 = ImageTk.PhotoImage(Image.open("img/bt1_1.png").resize((300, 90)))
bt2 = ImageTk.PhotoImage(Image.open("img/bt1_2.png").resize((300, 90)))
bt3 = ImageTk.PhotoImage(Image.open("img/bt1_3.png").resize((300, 90)))
bt4 = ImageTk.PhotoImage(Image.open("img/bt1_4.png").resize((250, 80)))

button_man_man = canvas.create_image(125, 150, anchor=tk.NW, image=bt1)
canvas.tag_bind(button_man_man,"<Button-1>",click_man_man)

button_man_bot = canvas.create_image(125, 265, anchor=tk.NW, image=bt2)
canvas.tag_bind(button_man_bot,"<Button-1>",click_man_bot)

button_bot_bot = canvas.create_image(125, 380, anchor=tk.NW, image=bt3)
canvas.tag_bind(button_bot_bot,"<Button-1>",click_bot_bot)

button_instruct = canvas.create_image(150, 530, anchor=tk.NW, image=bt4)
canvas.tag_bind(button_instruct,"<Button-1>",click_instruct)



view1.mainloop()

