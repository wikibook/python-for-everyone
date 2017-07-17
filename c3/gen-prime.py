# 소수를 반환하는 이터레이터
def genPrime(maxnum):
    num = 2
    while (num <= maxnum):
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0: # 소수가 아니다
                is_prime = False
                break
        if (is_prime): yield num
        num += 1

# 이터레이터를 얻는다
it = genPrime(50)
# 화면에 출력한다
for i in it:
    print(i, end=",")

