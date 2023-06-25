from tkinter import *

from PIL import ImageTk, Image


class Results:
    red = 0
    blue = 0
    kq = 0

    def __init__(self, red, blue, kq):
        self.red = red
        self.blue = blue
        self.kq = kq

    def show_results(self):
        global img
        results = Tk()
        results.title(" CỜ TOÁN VIỆT NAM")
        results.geometry("550x650+400+30")
        results.resizable(False, False)
        results.iconbitmap("img/logo.ico")
        canvas = Canvas(results, width=700, height=750)
        canvas.place(x=-2, y=-1)

        if self.kq == 1:
            img = ImageTk.PhotoImage(Image.open("img/red.png").resize((552, 652)))
        elif self.kq == 2:
            img = ImageTk.PhotoImage(Image.open("img/blue.png").resize((552, 652)))

        bg = canvas.create_image(0, 0, anchor=NW, image=img)

        text_red = "RED:  " + str(self.red)
        text_blue = "BLUE:  " + str(self.blue)

        lb_red = ImageTk.PhotoImage(Image.open("img/lb_red.png").resize((500, 150)))
        lb_blue = ImageTk.PhotoImage(Image.open("img/lb_blue.png").resize((500, 150)))
        bt_ok = ImageTk.PhotoImage(Image.open("img/bt_oke.png").resize((150, 70)))

        if self.kq == 1:
            label_red = canvas.create_image(25, 200, anchor=NW, image=lb_red)
            textred = canvas.create_text(270, 260, text=text_red, fill="#ffffff", font=("arial", 30, "bold"))
            label_blue = canvas.create_image(25, 400, anchor=NW, image=lb_blue)
            textblue = canvas.create_text(270, 460, text=text_blue, fill="#ffffff", font=("arial", 30, "bold"))
        elif self.kq == 2:
            label_blue = canvas.create_image(25, 200, anchor=NW, image=lb_blue)
            textblue = canvas.create_text(270, 260, text=text_blue, fill="#ffffff", font=("arial", 30, "bold"))
            label_red = canvas.create_image(25, 400, anchor=NW, image=lb_red)
            textred = canvas.create_text(270, 460, text=text_red, fill="#ffffff", font=("arial", 30, "bold"))

        button_ok = Button(
            results,
            image=bt_ok,
            border=0,
            bg="#abc2c7",
            activebackground="#abc2c7",
            command=results.destroy,
        )
        button_ok.place(x=200, y=550)

        results.mainloop()
