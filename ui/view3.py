import tkinter as tk
from tkinter import *

from PIL import ImageTk, Image

dept = 0

def click_start(event):
    global dept
    dept = scale.get()
    view3.destroy()

def click_back(event):
    global dept
    view3.destroy()
    dept = -1

def update_scale():
    text = "ĐỘ SÂU: " + str(scale.get())
    canvas.itemconfig(text_scale, text=text)
    canvas.after(15, update_scale)

view3 = tk.Tk()
view3.title("CỜ TOÁN VIỆT NAM")
view3.geometry("550x650+400+30")
view3.resizable(False, False)
view3.iconbitmap("img/logo.ico")
view3.configure(background="#769656")

canvas = tk.Canvas(view3, width=700, height=750)
canvas.place(x=-2, y=-1)

img = ImageTk.PhotoImage(Image.open("img/bg3_1.png").resize((552, 652)))
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

bt1 = ImageTk.PhotoImage(Image.open("img/bt3_1.png").resize((200, 70)))
bt2 = ImageTk.PhotoImage(Image.open("img/bt3_2.png").resize((200, 70)))
bt3 = ImageTk.PhotoImage(Image.open("img/bt3_3.png").resize((250, 90)))

scale = tk.Scale(
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
scale.place(x=70, y=250)
text = "ĐỘ SÂU:   " + str(scale.get())
label_scale = canvas.create_image(150, 350, anchor=tk.NW, image=bt3)
text_scale = canvas.create_text( 270,395,text=text,fill="#ffffff",font=("arial", 20, "bold"))

update_scale()

button_start = canvas.create_image(50, 500, anchor=tk.NW, image=bt1)
canvas.tag_bind(button_start,"<Button-1>",)

button_back = canvas.create_image(300, 500, anchor=tk.NW, image=bt2)
canvas.tag_bind(button_back,"<Button-1>",click_back)

view3.mainloop()
