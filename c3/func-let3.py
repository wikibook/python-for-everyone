# 함수를 인수로 받는 함수를 정의한다 --- (*1)
def calc_5_3(func):
    return func(5, 3)

# 곱셈을 계산하는 익명 함수를 인수로 준다 --- (*2)
result = calc_5_3(lambda a, b: a * b)
print(result) # 표시 결과→ 15

# 덧셈을 계산하는 익명 함수를 인수로 준다 --- (*3)
result = calc_5_3(lambda a, b: a + b)
print(result) # 표시 결과→ 8

