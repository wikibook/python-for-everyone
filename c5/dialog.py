# 대화상자를 표시하기 위해 필요한 모듈 --- (*1)
import tkinter.messagebox as mb

# 대화상자를 표시한다 --- (*2)
ans = mb.askyesno("질문", "라면을 좋아합니까?")
if ans == True:
    # OK 버튼밖에 없는 대화상자를 표시한다 --- (*3)
    mb.showinfo("동의", "저도 좋아합니다.")
else:
    mb.showinfo("정말로요?", "설마, 라면을 싫어하는 사람이 있을 줄이야!")
