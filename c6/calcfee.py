# 가격을 계산한다
import math

# 계산하는 클래스를 정의한다 --------- (*1)
class CalcFee:
    def __init__(self):
        ''' 초기화 처리 '''
        self.shipping_fee = 1000 # 배송료
        self.tax_rate = 0.08     # 세율
        self.value = 0           # 합계
        
    def addItem(self, price):
        ''' 상품 가격을 더한다 '''
        self.value += price 
        
    def calc(self):
        ''' 최종 요금을 계산한다 '''
        total = self.value + self.shipping_fee
        tax = math.ceil(total * self.tax_rate)
        v = math.ceil(total + tax)
        return v

# 실제로 계산하는 부분 ------------ (*2)
fee1 = CalcFee()
fee1.addItem(500)
print(fee1.calc(), "원")

fee2 = CalcFee()
fee2.shipping_fee = 1500
fee2.addItem(800)
fee2.addItem(500)
print(fee2.calc(), "원")
