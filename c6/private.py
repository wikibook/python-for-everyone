# 비공개 속성에 접근할 수 없다는 것을 확인하는 프로그램
# 따라서 이 프로그램에서는 오류가 발생합니다.
# --- 클래스를 정의한다
class Game:
    def __goal(self):
        print("비공개 메서드")
        
    def play(self):
        print("공개 메서드")

# --- 클래스를 이용한다
game = Game()
game.play()
game.__goal()        # 여기서 오류가 발생한다
