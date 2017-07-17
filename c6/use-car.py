# 정의한 클래스를 포함한 모듈을 임포트한다
import car

# 밴을 생성한다
car1 = car.Van("Gildong")
car1.turn_left()        # --- (*1) 슈퍼 클래스에 있는 메서드를 사용할 수 있다
car1.show_status()

# 캠핑카를 생성한다
car2 = car.Camper("Chulsoo")
car2.turn_right()
car2.show_status()
car2.make_ice()
