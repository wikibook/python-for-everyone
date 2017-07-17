# 함수 정의
def calcTime(dist, speed):
    t = dist / speed
    t = round(t, 1)
    return t

# 일반적인 호출 --- (*1)
print( calcTime(500, 100) )
# 키워드 인수를 사용한 호출 --- (*2)
print( calcTime(dist=500, speed=100) )


