from tkinter import *

root = Tk()
root.title("Samuel GUI")
root.geometry("640x480")

label1 = Label(root, text = "안녕하세요")
label1.pack()

photo = PhotoImage(file = "C:/Users/souls/PycharmProjects/Tkinter-project1/gui_basic/image.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
    global photo2  # 전역변수로 선언해야 garbage collection에서 수거를 안함.
    photo2 = PhotoImage(file = "C:/Users/souls/PycharmProjects/Tkinter-project1/gui_basic/image2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command = change)
btn.pack()

root.mainloop()
