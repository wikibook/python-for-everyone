class Pos:
    """ 좌표를 나타내는 클래스 """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """ + 연산자에 대한 처리를 정의한다
            self와 other에 일는 요소끼리 더한
            새로운 인스턴스를 반환한다 """
        x2 = self.x + other.x
        y2 = self.y + other.y
        return Pos(x2, y2)

    def __str__(self):
        """ 문자열을 반환한다 """
        return "({0}, {1})".format(self.x, self.y)

# 좌표 p1과 p2를 생성한다
p1 = Pos(10, 20)
p2 = Pos(30, 40)

# 연산자 '+'를 사용해본다
p3 = p1 + p2
print(p3)
