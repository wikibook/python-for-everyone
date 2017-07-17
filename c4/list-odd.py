# (1) 2배해서 1을 빼는 방법
data = [ (i * 2 - 1) for i in range(1, 6) ]
print(data)

# (2) range()를 조작하는 방법
data = [ i for i in range(1, 11, 2) ]
print(data)

# (3) 내장 표기로 for와 if를 조합하는 방법
data = [ i for i in range(1, 11) if i % 2 == 1 ]
print(data)

