# yield로 값을 반환하는 함수를 정의한다
def gen1to3():
    yield 1;
    yield 2;
    yield 3;

# 이터레이터 오브젝트를 만든다
it = gen1to3();
# for 구문에서 반복해서 표시한다
for i in it:
    print(i)

