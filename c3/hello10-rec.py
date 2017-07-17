# 재귀함수를 정의
def say_hello(i):
    if i <= 0: return
    print("hello", i)
    say_hello(i-1)
# 실행
say_hello(10)

