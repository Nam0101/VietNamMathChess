from tkinter import *

x = 3


def click_tt1():
    global x
    x = 1
    button_tt1.config(bg="#0812aa")
    button_tt2.config(bg="#595fae")
    buttontt3.config(bg="#595fae")


def click_tt2():
    global x
    x = 2
    button_tt1.config(bg="#595fae")
    button_tt2.config(bg="#0812aa")
    buttontt3.config(bg="#595fae")


def clicktt3():
    global x
    x = 3
    button_tt1.config(bg="#595fae")
    button_tt2.config(bg="#595fae")
    buttontt3.config(bg="#0812aa")


def click_next():
    view2.destroy()
    import view3


def click_back():
    view2.destroy()
    import view1


view2 = Tk()
view2.title(" CỜ TOÁN VIỆT NAM")
view2.geometry("600x600+400+50")
view2.resizable(False, False)
view2.iconbitmap("../img/logo.ico")
view2.configure(background="#769656")

label_title = Label(
    view2,
    text="CHỌN THUẬT TOÁN",
    bg="#769656",
    fg="#8cfffb",
    font=("monaco", 35, "bold"),
)
label_title.place(x=90, y=50)

button_tt1 = Button(
    view2,
    text="THUẬT TOÁN 1",
    width=15,
    height=1,
    bg="#595fae",
    fg="#ffffff",
    font=("arial", 20, "bold"),
    command=click_tt1,
)
button_tt1.place(x=170, y=150)


button_tt2 = Button(
    view2,
    text="THUẬT TOÁN 2",
    width=15,
    height=1,
    bg="#595fae",
    fg="#ffffff",
    font=("arial", 20, "bold"),
    command=click_tt2,
)
button_tt2.place(x=170, y=250)


buttontt3 = Button(
    view2,
    text="THUẬT TOÁN 3",
    width=15,
    height=1,
    bg="#595fae",
    fg="#ffffff",
    font=("arial", 20, "bold"),
    command=clicktt3,
)
buttontt3.place(x=170, y=350)

button_back = Button(
    view2,
    text="QUAY LẠI",
    width=10,
    height=1,
    bg="#b97a56",
    fg="#ffffff",
    font=("arial", 18, "bold"),
    command=click_back,
)
button_back.place(x=90, y=480)

button_next = Button(
    view2,
    text="TIẾP TỤC",
    width=10,
    height=1,
    bg="#0ed145",
    fg="#ffffff",
    font=("arial", 18, "bold"),
    command=click_next,
)
button_next.place(x=350, y=480)

view2.mainloop()
