# tkinter를 임포트한다 --- (*1)
from tkinter import *
import tkinter.messagebox as mb

# 사용자가 버튼을 눌렀을 때 실행해야 할 작업을 함수로 정의한다 --- (*2)
def say_hello():
    mb.showinfo("인사","안녕하세요.")

# 메인 창을 생성한다 --- (*3)
root = Tk()
root.title('인사') # 메인 창에 타이틀을 설정한다

# 레이블을 생성한다 --- (*4)
desc_label = Label(text="아래의 버튼을 눌러주세요.")
desc_label.pack()

# 인사 버튼을 생성한다 --- (*5)
hello_button = Button(
    text="인사",        # 버튼에 표시하는 텍스트
    width=10, height=3, # 문자 수에 맞춰 버튼 크기를 지정한다
    command=say_hello   # 버튼을 클릭했을 때 실행할 작업
)
hello_button.pack()

# 메인 루프를 시작한다 --- (*6)
root.mainloop()
