# 화면에 많은 선을 긋는다

# 그래픽 라이브러리를 가져온다
from tkinter import *
# 화면 초기화
w = Canvas(Tk(), width=400, height=300)
w.pack()

# 많은 선을 긋는다
for i in range(100):
    y = i * 3
    if i % 2 == 0:
        c = "#ff0000" # red
    else:
        c = "#0000FF" # blue
    w.create_line(0, 0, 400, y, fill=c)

mainloop()
