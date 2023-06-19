from tkinter import *

from PIL import ImageTk, Image

thuat_toan = 1


def click_tt1():
    global thuat_toan
    thuat_toan = 1
    view2.destroy()


def click_tt2():
    global thuat_toan
    thuat_toan = 2
    view2.destroy()


def clicktt3():
    global thuat_toan
    thuat_toan = 3
    view2.destroy()


def click_back():
    # view2.withdraw()
    view2.destroy()

    # view1.show_view1()


view2 = Tk()
view2.title(" CỜ TOÁN VIỆT NAM")
view2.geometry("600x650+400+30")
view2.resizable(False, False)
view2.iconbitmap("img/logo.ico")
img = ImageTk.PhotoImage(Image.open("img/bg2.png").resize((600, 650)))
panel = Label(view2, image=img)
panel.place(x=0, y=0, relwidth=1, relheight=1)

bt1 = ImageTk.PhotoImage(Image.open("img/bt2_1.png").resize((300, 70)))
bt2 = ImageTk.PhotoImage(Image.open("img/bt2_2.png").resize((300, 70)))
bt3 = ImageTk.PhotoImage(Image.open("img/bt2_3.png").resize((300, 70)))
bt4 = ImageTk.PhotoImage(Image.open("img/bt2_4.png").resize((300, 70)))

button_tt1 = Button(
    view2,
    image=bt1,
    bg="#353554",
    border=0,
    command=click_tt1,
)
button_tt1.place(x=150, y=170, width=300, height=70)

button_tt2 = Button(
    view2,
    image=bt2,
    bg="#353554",
    border=0,
    command=click_tt2,
)
button_tt2.place(x=150, y=300, width=300, height=70)

buttontt3 = Button(
    view2,
    image=bt3,
    bg="#353554",
    border=0,
    command=clicktt3,
)
buttontt3.place(x=150, y=430, width=300, height=70)

button_back = Button(
    view2,
    image=bt4,
    bg="#373b78",
    border=0,
    command=click_back,
)
button_back.place(x=150, y=550, width=300, height=70)

view2.mainloop()
