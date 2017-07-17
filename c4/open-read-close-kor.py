# (1) 텍스트 파일을 연다
a_file = open("mt7_7_euckr.txt", encoding="euc-kr")

# (2) 텍스트를 읽는다
s = a_file.read()

# (3) 파일을 닫는다
a_file.close()

# 결과를 표시한다
print(s)

