# 학, 거북이, 문어, 오징어를 나타내는 클래스를 정의한다 --- (*1)
class Crane:
    def get_name(self):
        return "학"
    def get_legs(self):
        return 2

class Turtle:
    def get_name(self):
        return "거북이"
    def get_legs(self):
        return 4

class Octopus:
    def get_name(self):
        return "문어"
    def get_legs(self):
        return 8

class Squid:
    def get_name(self):
        return "오징어"
    def get_legs(self):
        return 10

# 학거북산 문제를 푸는 함수 --- (*2)
def calc_craneturtle(crane, turtle, heads, legs):
    crane_l = crane.get_legs()
    turtle_l = turtle.get_legs()
    crane_name = crane.get_name()
    turtle_name = turtle.get_name()
    turtle_num = (legs - (crane_l * heads)) // (turtle_l - crane_l)
    crane_num = heads - turtle_num
    print("---")
    print("머리=", heads, "다리=", legs)
    print(crane_name, "=", crane_num)
    print(turtle_name, "=", turtle_num)
    return (crane_num, turtle_num)


# 모듈이 아닐 때는 다음을 실행한다 --- (*3)
if __name__ == '__main__':
    # 학거북산으로 문제를 푼다
    calc_craneturtle(Crane(), Turtle(), heads=10, legs=28)
    calc_craneturtle(Octopus(), Squid(),  heads=11, legs=100)
