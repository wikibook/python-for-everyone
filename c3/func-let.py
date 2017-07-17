# 함수를 정의
def mul_func(a, b):
    return a * b

def div_func(a, b):
    return a / b

# mul_func 함수를 변수에 대입 --- (*1)
func = mul_func
# 대입한 변수에서 함수를 사용한다 --- (*2)
result = func(2, 3)
print(result) # 표시된 결과→ 6

# div_func 함수를 변수에 대입할 경우 --- (*3)
func2 = div_func
result = func2(10, 5)
print(result) # 표시된 결과→ 2.0



