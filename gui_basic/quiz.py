import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480") #가로 x 세로
# root.geometry("640x480+100+300") # 가로 세로 x좌표 y좌표

menu = Menu(root)

# 열기, 저장 파일 이름
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): #파일 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 현재 창에 있는 내용 삭제
            txt.insert(END, file.read()) # 읽어온 내용 화면에 출력

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))


menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# 빈 메뉴들
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")


# 본문영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)


root.config(menu=menu)
root.mainloop()
