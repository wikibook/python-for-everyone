# BMI를 계산하는 클래스
class BMI:
    def __init__(self, weight, height):
        ''' 초기화 '''
        self.weight = weight
        self.height = height
        self.calcBMI()

    def calcBMI(self):
        ''' BMI를 계산한다 '''
        h = self.height / 100
        self.bmi = self.weight / (h ** 2)

    def printJudge(self):
        ''' 결과를 표시한다 '''
        print("---")
        print("BMI=", self.bmi)
        b = self.bmi
        if (b < 18.5): print("마름")
        elif (b < 25): print("표준")
        elif (b < 30): print("가벼운 비만")
        else: print("심각한 비만")

# 첫 번째 사람
person1 = BMI(weight=65, height=170)
person1.printJudge()

# 두 번째 사람
person2 = BMI(76, 165)
person2.printJudge()

# 세 번째 사람
person3 = BMI(50, 180)
person3.printJudge()
