from tkinter import *
from tkinter import messagebox

def myFunc():
    # messagebox.showinfo("우주 버튼", "크다")
    if chk.get() == 0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요")
    else : 
        messagebox.showinfo("", "체크버튼이 켜졌어요")

window = Tk()
window.title("연습용")
window.geometry("500x500")

chk = IntVar()
cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc)

cb1.pack()

# window.resizable(width=False, height=False)
# label1 = Label(window, text="문자열1")
# label2 = Label(window, text="문자열2", font=("궁서체", 30), fg="red")
# label3 = Label(window, text="문자열3", bg="magenta", width=100, height=100, anchor=SE)
# photo = PhotoImage(file="a.gif")
# photo2 = PhotoImage(file="lex1.gif")
# photo3 = PhotoImage(file="lex.gif")

# button1 = Button(window, image=photo, command=myFunc)

# label4 = Label(window, image=photo)
# label5 = Label(window, image=photo2)
# label6 = Label(window, image=photo3)

# button1.pack()

# label1.pack()
# label2.pack()
# label3.pack()
# label4.pack(side=RIGHT)
# label5.pack(side=LEFT)
# label6.pack()

window.mainloop()