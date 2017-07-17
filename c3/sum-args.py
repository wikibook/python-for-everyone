def sumArgs(*args):
    v = 0
    for n in args:
        v += n
    return v

# 합계를 표시
print(sumArgs(1, 2,3))
print(sumArgs(1, 2, 3, 4, 5))
print(sumArgs(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

