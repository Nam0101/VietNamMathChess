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
        results.geometry("600x650+400+30")
        results.resizable(False, False)
        results.iconbitmap("img/logo.ico")
        if self.kq == 1:
            img = Image.open("img/red.png")
        elif self.kq == 2:
            img = Image.open("img/blue.png")
        img = img.resize((600, 650), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(results, image=img)
        panel.place(x=0, y=0)

        text = "RED\n" + str(self.red)
        imgbutton = ImageTk.PhotoImage(Image.open("img/button1.png").resize((120, 120)))
        Label_red = Label(
            results,
            text=text,
            font=("Arial", 25, "bold"),
            fg="#ec0000",
            image=imgbutton,
            compound="center",
        )
        Label_red.place(x=100, y=330, width=120, height=120)

        text = "BLUE\n" + str(self.blue)
        Label_blue = Label(
            results,
            image=imgbutton,
            text=text,
            font=("Arial", 25, "bold"),
            fg="#2100f5",
            compound="center",
        )
        Label_blue.place(x=380, y=330, width=120, height=120)

        img_oke = ImageTk.PhotoImage(Image.open("img/bt_oke.png").resize((100, 100)))
        button_oke = Button(
            panel,
            image=img_oke,
            bg="#3a3d70",
            # command=results.destroy,
        )
        button_oke.place(x=250, y=500, width=100, height=100)

        results.mainloop()


Results = Results(1, 2, 1)
Results.show_results()
