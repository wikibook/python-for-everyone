# tkinter를 임포트 --- (*1)
from tkinter import *

# 텍스트 문자 개수를 세는 함수 --- (*2)
def count_text(event):
    s = main_text.get(1.0, END)
    info_label.config(text="{0}문자".format(len(s)))

# 메인 창을 생성한다 --- (*3)
root = Tk()
root.title('텍스트 카운터')

# 텍스트 상자를 생성한다 --- (*4)
main_text = Text(root)
main_text.bind("<Key>", count_text) # 이벤트를 설정한다 --- (*5)
main_text.pack()

# 문자 개수를 표시하는 레이블을 생성한다 --- (*6)
info_label = Label(root)
info_label.pack()

# 메인 루프를 시작한다 --- (*7)
root.mainloop()
