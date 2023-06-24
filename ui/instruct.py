from tkinter import *


# def show_instruct():
#     instruct.deiconify()


instruct = Tk()
instruct.title(" CỜ TOÁN VIỆT NAM")
instruct.geometry("600x600+375+70")
instruct.resizable(False, False)
instruct.iconbitmap("img/logo.ico")
instruct.configure(background="#769656")

label_title = Label(
    instruct, text="HƯỚNG DẪN", font=("Arial", 20, "bold"), bg="#769656", fg="#0812aa"
)
label_title.pack(pady=10)
text = Text(
    instruct,
    height=10,
    width=50,
    font=("Arial", 15),
    wrap="word",
    padx=10,
    pady=10,
    spacing3=28,
    bg="#769656",
    fg="#0812aa",
    relief="flat",
    highlightthickness=0,
)
text.place(x=10, y=50)
scrollbar = Scrollbar(instruct, orient="vertical", command=text.yview)
scrollbar.place(x=580, y=70, height=500)
text.insert(
    "1.0",
    "- Ngoại trừ quân số 0 không được phép di chuyển, các quân còn lại 1-9 đều có thể đi theo hàng ngang, cột dọc, đường chéo. Mỗi ô trống trên bàn cờ là một bước đi. Số bước đi tối đa được thực hiện theo trị số riêng của từng quân cờ. Chẳng hạn, số 2 có thể đi tối đa 2 ô trống, số 9 có thể đi tối đa 9 ô trống tùy mục đích của người chơi. Các quân cờ không được phép nhảy qua đầu các quân khác.\n"
    + "- Khi muốn bắt quân của đối phương, điều kiện là bên mình phải có hai quân đứng trong hai ô liền nhau theo chiều dọc hoặc ngang hoặc chéo (để tạo thành một phép tính và phía trước không có quân của đối phương đứng cản). Sau đó dùng các phép cộng (+), hoặc trừ (-), hoặc nhân (x), hoặc chia (:) với nhau để ra đáp số. Đáp số của mỗi phép tính là điểm có thể bắt được quân của đối phương.\n"
    + "- Chẳng hạn, bên mình có quân 8 và quân 5 đứng liền nhau (8 đứng dưới, 5 đứng trên) theo hàng dọc thì có thể lấy 8-5=3 hoặc 8+5=13 để bắt quân đang đứng ở ô thứ ba của đối phương (tính từ ô của quân 5 đứng trước) nếu muốn đánh tiến. Sau đó, lấy quân số 8 thế vào vị trí mà quân số của đối phương bị bắt. Còn nếu muốn bắt lùi thì lấy 5+8=13 và bắt quân đang đứng ở ô thứ 3 bắt đầu tính từ quân số 8.\n"
    + "- Chú ý: Nếu kết quả của phép cộng hoặc nhân mà lớn hơn 10 thì chỉ lấy số của hàng đơn vị để tính điểm bắt quân. Chẳng hạn 5+8=13 thì 3 là điểm để bắt quân của đối phương. Nếu là phép chia có dư thì có thể lấy số dư để bắt quân. Chẳng hạn, lấy quân 8 chia cho quân 5 bằng 1 dư 3 thì ô cờ được bắt quân của đối phương là ô cách quân 5 là 1 hoặc 3 ô. Không thể lấy 5x8=40 vì điểm 0 là không có giá trị.\n"
    + "- Trong khi tính toán, nếu phía trước có quân của đối phương đứng cản thì không thể bắt được quân của đối phương. Chẳng hạn 8+5=13 thì có thể bắt được quân số bất kỳ của đối phương (1, 2, 3, 4...) đang đứng ở ô thứ 3 tính từ quân số 5 của bên mình, nhưng nếu ở ô thứ 1, 2 có quân đối phương đang đứng thì không thể bắt được quân ở ô thứ 3 kể trên.\n"
    + "- Trong quá trình chơi, bất kể khi nào, cứ bắt được quân số 0 của đối phương là thắng tuyệt đối. Tuy nhiên, nếu không bắt được quân số 0 vẫn có thể tính việc thắng - thua bằng cách dựa theo số điểm. Mỗi quân cờ có số điểm tính theo trị số của nó. Chẳng hạn quân số 1 là 1 điểm, số 2 là 2 điểm... Trước khi chơi, hai bên có thể thỏa thuận thang điểm cho mỗi ván là 10-15-20-...-45 điểm và chơi 1-3-5-7... ván. Sau đó tính trên tổng số ván thắng để tính thắng - thua. Nhưng trong quá trình thi đấu, bên nào bị đối phương bắt quân số 0 là bị xử thua tuyệt đối - dù trước đó đang dẫn trước 1-2-3-4-... ván. Ví dụ:\n"
    + "•	Ván 1: A thắng B với tỉ số 10-7\n"
    + "•	Ván 2: A thắng B với tỉ số 12-5\n"
    + "•	Ván 3: B thắng A tuyệt đối (tức B bắt được quân số 0 của A).\n"
    + "=>Kết quả cuối cùng: B thắng A chung cuộc.\n",
)
text.config(yscrollcommand=scrollbar.set)

instruct.mainloop()
