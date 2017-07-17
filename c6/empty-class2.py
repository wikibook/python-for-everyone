# 빈 클래스
class Empty : pass

# 빈 클래스의 인스턴스를 생성한다
calc = Empty()
# 메서드를 동적으로 추가한다
calc.x2 = lambda x : x * 2
calc.x3 = lambda x : x * 3

# 추가한 메서드를 사용해본다
print( calc.x2(8) )
print( calc.x3(5) )


