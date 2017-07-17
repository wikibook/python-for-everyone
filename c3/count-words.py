# 단어의 출현 횟수를 센다
text = """
Keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

# 단어를 구분한다 --- (*1)
text = text.replace(";", "")
text = text.replace(",", "")
text = text.replace(".", "")
words = text.split()

# 단어를 센다 --- (*2)
counter = {}
for w in words:
    ws = w.lower() # 소문자로 변환한다
    if ws in counter:
        counter[ws] += 1
    else:
        counter[ws] = 1

# 결과를 표시한다 --- (*3)
for k,v in sorted(counter.items()):
    if v >= 3:
        print(k, v)
