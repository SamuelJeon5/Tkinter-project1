from tkinter import *

root = Tk()
root.title("Samuel GUI")
root.geometry("640x480") #가로 x 세로

chkvar = IntVar() #chkvar에 int형으로 값을 저장한다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() #자동 선택처리
# chkbox.deselect() #선택 해제처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()
def btncmd():
    print(chkvar.get()) #숫자 0: 체크해제, 1: 체크
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()
