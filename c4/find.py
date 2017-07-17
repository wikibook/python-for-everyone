# 텍스트 파일에서 키워드를 검색한다
key = "find"
with open("mt7_7.txt", encoding="utf-8") as tf:
    # 파일을 한 행씩 읽는다
    for i, line in enumerate(tf):
        # 문자열 key가 행에 포함되어 있는가?
        if line.find(key) >= 0:
            print(i+1, ":", line)

