from tkinter import *

root = Tk()
root.title("Samuel GUI")
root.geometry("640x480")  # 가로 x 세로

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

#File menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New file", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

#Edit menu(빈값)

menu.add_cascade(label="Edit")

#Language 메뉴 추가(라디오 버튼을 통해 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="C")
menu_lang.add_radiobutton(label="C++")
menu_lang.add_radiobutton(label="Java")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴 추가
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap1")
menu_view.add_checkbutton(label="Show Minimap2")
menu_view.add_checkbutton(label="Show Minimap3")

menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop()
