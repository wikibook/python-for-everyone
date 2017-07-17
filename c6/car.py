# 기저 클래스를 정의한다
class Car:
    ''' 기본적인 기능을 갖춘 자동차를 나타내는 클래스 '''
    def __init__(self, owner):
        self.handle = 0
        self.car_type = "normal"
        self.owner = owner

    def turn_left(self):
        ''' 핸들을 왼쪽으로 꺾는다 '''
        self.handle -= 90

    def turn_right(self):
        ''' 핸들을 오른쪽으로 꺾는다 '''
        self.handle += 90

    def show_status(self):
        ''' 상태를 표시한다 '''
        print("---")
        print("owner:", self.owner)
        print("car_type:", self.car_type)
        print("handle:", self.handle)

# 파생 클래스를 정의한다
class Van(Car):
    ''' 밴 클래스 '''
    def __init__(self, owner):
        super().__init__(owner)
        self.car_type = "van"

    def open_door(self):
        ''' 문을 자동으로 연다 '''
        print("문을 열었습니다.")

    def close_door(self):
        ''' 문을 자동으로 닫는다 '''
        print("문을 닫았습니다.")

class Camper(Car):
    ''' 캠핑카 클래스 '''
    def __init__(self, owner):
        super().__init__(owner)
        self.car_type = "camper"

    def make_ice(self):
        ''' 얼음을 만든다 '''
        print("얼음을 만들었습니다.")
