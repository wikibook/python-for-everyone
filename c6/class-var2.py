class Cat:
    # 클래스 변수
    cat_sound = "nya-"
    # 메서드
    def sounds(self):
        print(self.cat_sound) # ← 이곳을 변경했다(*1)

mike = Cat()
nora = Cat()

# 울음소리를 변경한다
mike.cat_sound = "myu-" # --- (*2)
mike.sounds()
nora.sounds()


