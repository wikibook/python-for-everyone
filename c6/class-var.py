class Cat:
    # 클래스 변수
    cat_sound = "nya-"
    # 메서드
    def sounds(self):
        print(Cat.cat_sound)

mike = Cat()
mike.sounds() # nya-

nora = Cat()
nora.sounds() # nya-

# 여기서 클래스 변수를 변경한다
Cat.cat_sound = "myu-"

# 그러면 모든 인스턴스에서 값이 변경된다
nora.sounds() # myu-
mike.sounds() # myu-
