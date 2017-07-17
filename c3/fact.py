# 계승을 구한다
def fact(n):
    if n == 0: # 인수가 0이면 1을 반환한다
        return 1
    else: # 그외의 경우에는 fact()를 재귀적으로 호출한다
        return n * fact(n-1)

print(fact(3))
print(fact(5))

