import tkinter as tk

from PIL import ImageTk, Image

algo = 0

def click_tt1(event):
    global algo
    algo = 1
    view3.destroy()

def click_tt2(event):
    global algo
    algo = 2
    view3.destroy()

def click_tt3(event):
    global algo
    algo = 3
    view3.destroy()

def click_tt4(event):
    global algo
    algo = 4
    view3.destroy()

def click_back(event):
    global algo
    view3.destroy()
    algo = -1

view3 = tk.Tk()
view3.title(" CỜ TOÁN VIỆT NAM")
view3.geometry("550x650+400+30")
view3.resizable(False, False)
view3.iconbitmap("img/logo.ico")

canvas = tk.Canvas(view3, width=700, height=750)
canvas.place(x=-2, y=-1)

img = ImageTk.PhotoImage(Image.open("img/bg2.png").resize((552, 652)))
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

bt1 = ImageTk.PhotoImage(Image.open("img/bt2_1.png").resize((300, 70)))
bt2 = ImageTk.PhotoImage(Image.open("img/bt2_2.png").resize((300, 70)))
bt3 = ImageTk.PhotoImage(Image.open("img/bt2_3.png").resize((300, 70)))
bt4 = ImageTk.PhotoImage(Image.open("img/bt2_4.png").resize((300, 70)))
bt5 = ImageTk.PhotoImage(Image.open("img/bt2_5.png").resize((300, 70)))

button_tt1 = canvas.create_image(125, 130, anchor=tk.NW, image=bt1)
canvas.tag_bind(button_tt1,"<Button-1>",click_tt1)

button_tt2 = canvas.create_image(125, 220, anchor=tk.NW, image=bt2)
canvas.tag_bind(button_tt2,"<Button-1>",click_tt2)

button_tt3 = canvas.create_image(125, 310, anchor=tk.NW, image=bt3)
canvas.tag_bind(button_tt3,"<Button-1>",click_tt3)

button_tt4 = canvas.create_image(125, 400, anchor=tk.NW, image=bt4)
canvas.tag_bind(button_tt4,"<Button-1>",click_tt4)

button_back = canvas.create_image(125, 540, anchor=tk.NW, image=bt5)
canvas.tag_bind(button_back,"<Button-1>",click_back)

view3.mainloop()
