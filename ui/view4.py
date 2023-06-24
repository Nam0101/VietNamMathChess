import tkinter as tk
from tkinter import *

from PIL import ImageTk, Image

dept1 = 0
dept2 = 0

def click_start(event):
    global dept1, dept2
    dept1 = scale1.get()
    dept2 = scale2.get()
    view3.destroy()

def click_back(event):
    global dept1, dept2
    view3.destroy()
    dept1 = -1
    dept2 = -1


def update_scale():
    text1 = "ĐỘ SÂU 1: " + str(scale1.get())
    text2 = "ĐỘ SÂU 2: " + str(scale2.get())
    canvas.itemconfig(text_scale1, text=text1)
    canvas.itemconfig(text_scale2, text=text2)
    canvas.after(15, update_scale)


view3 = tk.Tk()
view3.title("CỜ TOÁN VIỆT NAM")
view3.geometry("550x650+400+30")
view3.resizable(False, False)
view3.iconbitmap("img/logo.ico")
view3.configure(background="#769656")

canvas = tk.Canvas(view3, width=700, height=750)
canvas.place(x=-2, y=-1)

img = ImageTk.PhotoImage(Image.open("img/bg3_2.png").resize((552, 652)))
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

bt1 = ImageTk.PhotoImage(Image.open("img/bt3_1.png").resize((200, 70)))
bt2 = ImageTk.PhotoImage(Image.open("img/bt3_2.png").resize((200, 70)))
bt3 = ImageTk.PhotoImage(Image.open("img/bt3_3.png").resize((250, 90)))

scale1 = tk.Scale(
    view3,
    from_=1,
    to=5,
    bg="blue",
    fg="#ffffff",
    font=("arial", 20, "bold"),
    border=0,
    orient=HORIZONTAL,
    length=400,
)
scale1.place(x=70, y=150)
text1 = "ĐỘ SÂU 1: " + str(scale1.get())
label_scale1 = canvas.create_image(150, 200, anchor=tk.NW, image=bt3)
text_scale1 = canvas.create_text( 270,245,text=text1,fill="#ffffff",font=("arial", 20, "bold"))

scale2 = tk.Scale(
    view3,
    from_=1,
    to=5,
    bg="red",
    fg="#ffffff",
    font=("arial", 20, "bold"),
    border=0,
    orient=HORIZONTAL,
    length=400,
)
scale2.place(x=70, y=350)
text2 = "ĐỘ SÂU 2: " + str(scale2.get())
label_scale2 = canvas.create_image(150, 400, anchor=tk.NW, image=bt3)
text_scale2 = canvas.create_text( 270,445,text=text2,fill="#ffffff",font=("arial", 20, "bold"))

update_scale()

button_start = canvas.create_image(50, 550, anchor=tk.NW, image=bt1)
canvas.tag_bind(button_start, "<Button-1>", click_start)

button_back = canvas.create_image(300, 550, anchor=tk.NW, image=bt2)
canvas.tag_bind(button_back, "<Button-1>", click_back)

view3.mainloop()
