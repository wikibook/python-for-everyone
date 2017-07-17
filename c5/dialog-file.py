# 대화상자를 표시하는 데에 필요한 모듈
import tkinter.filedialog as fd

# 파일 선택 대화상자를 표시한다
path = fd.askopenfilename(
    title="처리 대상 파일을 지정해주세요.",
    filetypes=[('HTML','.html')])
print(path)
