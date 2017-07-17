# 꽃가게에 지불한 금액을 구한다
# 가격
rose_v = 500
sun_v = 400
tulip_v = 700
# 개수
rose_c = 18
sun_c = 8 - 2
tulip_c = 21 - 5
# 할인율
rate = 0.9
# 계산
sum_v = (rose_v * rose_c) + (sun_v * sun_c) + (tulip_v * tulip_c)
payment = sum_v * rate
# 결과를 표시
print("총 구매 금액은", sum_v, "원")
print("할인받으면", payment, "원")
