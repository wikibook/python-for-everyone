# 30 이하의 홀수를 반환하는 이터레이터
def genOdd():
    i = 1
    while i <= 30:
        yield i
        i += 2

# 이터레이터를 얻는다
it = genOdd()
for v in it:
    print(v, end=",")


