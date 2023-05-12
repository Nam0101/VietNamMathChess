from tkinter import *

x = 3


def click_nguoi_nguoi():
    global x
    x = 1
    button_nguoi_nguoi.config(bg="#0812aa")
    button_nguoi_may.config(bg="#595fae")
    button_may_may.config(bg="#595fae")


def click_nguoi_may():
    global x
    x = 2
    button_nguoi_nguoi.config(bg="#595fae")
    button_nguoi_may.config(bg="#0812aa")
    button_may_may.config(bg="#595fae")


def click_may_may():
    global x
    x = 3
    button_nguoi_nguoi.config(bg="#595fae")
    button_nguoi_may.config(bg="#595fae")
    button_may_may.config(bg="#0812aa")


def click_huong_dan():
    pass


def click_next():
    view1.destroy()
    if x == 1:
        import view3
    else:
        import view2


view1 = Tk()
view1.title(" CỜ TOÁN VIỆT NAM")
view1.geometry("600x600+400+50")
view1.resizable(False, False)
view1.iconbitmap("D:\Tri_tue_nhan_tao\img\logo.ico")
view1.configure(background="#769656")

label_title = Label(
    view1,
    text="CỜ TOÁN VIỆT NAM",
    bg="#769656",
    fg="#8cfffb",
    font=("monaco", 35, "bold"),
)
label_title.place(x=100, y=50)

button_nguoi_nguoi = Button(
    view1,
    text="CHƠI VỚI NGƯỜI",
    width=15,
    height=1,
    bg="#595fae",
    fg="#ffffff",
    font=("arial", 20, "bold"),
    command=click_nguoi_nguoi,
)
button_nguoi_nguoi.place(x=170, y=150)


button_nguoi_may = Button(
    view1,
    text="CHƠI VỚI MÁY",
    width=15,
    height=1,
    bg="#595fae",
    fg="#ffffff",
    font=("arial", 20, "bold"),
    command=click_nguoi_may,
)
button_nguoi_may.place(x=170, y=250)


button_may_may = Button(
    view1,
    text="MÁY VS MÁY",
    width=15,
    height=1,
    bg="#595fae",
    fg="#ffffff",
    font=("arial", 20, "bold"),
    command=click_may_may,
)
button_may_may.place(x=170, y=350)

button_huong_dan = Button(
    view1,
    text="HƯỚNG DẪN",
    width=10,
    height=1,
    bg="#b86637",
    fg="#ffffff",
    font=("arial", 18, "bold"),
    command=click_huong_dan,
)
button_huong_dan.place(x=90, y=480)

button_next = Button(
    view1,
    text="TIẾP TỤC",
    width=10,
    height=1,
    bg="#0ed145",
    fg="#ffffff",
    font=("arial", 18, "bold"),
    command=click_next,
)
button_next.place(x=350, y=480)


view1.mainloop()
