class Pos:
    """ 좌표를 나타내는 클래스 """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x2 = self.x + other.x
        y2 = self.y + other.y
        return Pos(x2, y2)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x2 = self.x * other
            y2 = self.y * other
            return Pos(x2, y2)
        else:
            raise TypeError

    def __str__(self):
        """ 문자열을 반환한다 """
        return "({0}, {1})".format(self.x, self.y)

# 좌표 p1
p1 = Pos(10, 20)

# 연산자 '*'를 사용해본다
p2 = p1 * 1.7
print(p2)
