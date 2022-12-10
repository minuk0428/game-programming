from tkinter import *
from tkinter import messagebox

#함수 선언부
def myFunc():
    #messagebox.showinfo("버튼 클릭","버튼 누름?")
    if chk.get() == 0:
        messagebox.showinfo("","체크버튼 OFF")
    else :
        messagebox.showinfo("","체크버튼 On")
    
#코드 메인부
root = Tk()
root.geometry("500x500")    
root.title("창 조절 연습")

chk = IntVar()  #Tkinter에서 사용할 수 있는 정수형 객체 생성
cb1 = Checkbutton(root, text="클릭하세요",variable=chk, command=myFunc)
cb1.pack()

#root.resizable(width = TRUE, height = TRUE)  #창 조절

button1 = Button(root, text="클릭하세요", bg="yellow",fg="red", command=myFunc,width=30,height=10,anchor=CENTER)
button1.pack()

label1 = Label(root, text="난생처음~~ python을")
label1.pack()    #pack에 의해 윈도우에 라벨이 붙음

label2 = Label(root, text="열심히", font=("궁서체", 70), fg="red")
label2.pack()

label3 = Label(root, text="코딩중", bg="yellow",width=40,height=8,anchor=CENTER)
label3.pack()

root.mainloop()

