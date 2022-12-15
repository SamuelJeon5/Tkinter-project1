import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("Samuel GUI")
root.geometry("640x480") #가로 x 세로


def btncmd():
    pass

btn = Button(root, text="선택", command=btncmd)
btn.pack()
root.mainloop()
