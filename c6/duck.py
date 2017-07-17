# 어떤 인스턴스에 있는 sound와 walk 메서드를 실행한다
def test_duck(it):
    it.sound()
    it.walk()

# 클래스를 정의한다
class Duck:
    def sound(self):
        print('꽥꽥')
    def walk(self):
        print("거위가 걸어간다")

class Dog:
    def sound(self):
        print("멍멍")
    def walk(self):
        print("개가 걸어간다")

class Cat:
    def sound(self):
        print("야옹")
    def walk(self):
        print("고양이가 걸어간다")

# 덕 타이핑
ori = Duck()
test_duck(ori)

gae = Dog()
test_duck(gae)

goyang_i = Cat()
test_duck(goyang_i)
