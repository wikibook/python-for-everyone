# 함수를 정의한다
def mul_func(a, b): return a * b
def add_func(a, b): return a + b

# 함수를 인수로 받는 함수를 정의한다 --- (*1)
def calc_5_3(func):
    return func(5, 3) # --- (*1a)

# 함수를 인수로 지정한다 --- (*2)
result = calc_5_3(mul_func)
print(result) # 표시된 결과→ 15

# 다른 함수를 인수로 지정한다 --- (*3)
result = calc_5_3(add_func)
print(result) # 표시된 결과 → 8

