class SuperClass:
    def blar(self, id):
        print("---")
        print("SuperClass.blar=", id)

class SubClass(SuperClass):
    def blar(self, id):
        super().blar(id)             # 기저 클래스의 blar 메서드를 호출한다
        print("SubClass.blar=", id)


# 기저 클래스의 blar 메서드를 실행한다
rc = SuperClass()
rc.blar(100)

# 파생 클래스의 blar 메서드를 실행한다
sc = SubClass()
sc.blar(300)
