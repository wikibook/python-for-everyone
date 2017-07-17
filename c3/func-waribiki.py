# 슈퍼마켓 할인 계산

def calcValue(who, hour, count, value):
    '''어떤 슈퍼마켓의 할인 금액을 계산하는 함수'''
    info = "할인 없음"
    # 14시에 상품을 3개 이상 구매하면 10% 할인
    if (hour == 14) and (count >= 3):
        value *= 0.9
        info = "10% 할인"
    # 15시에 상품을 5개 이상 구매하면 20% 할인
    elif (hour == 15) and (count >= 5):
        value *= 0.8
        info = "20% 할인"
    # 결과 표시
    value = int(value)
    print("{0}씨는 {1}={2}원".format(who, info, value))

# A/B/C씨 각각 지불할 금액을 구한다
calcValue("A", 15, 3, 12000)
calcValue("B", 14, 5, 20000)
calcValue("C", 15, 8, 54000)

