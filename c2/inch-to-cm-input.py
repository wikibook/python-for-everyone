# 입력을 받아서 인치를 센티미터로 변환한다
# 변환해야 하는 값
per_inch = 2.54
# 사용자로부터 입력을 받는다
user = input("몇 인치입니까?")
# 부동소수점형으로 변환한다
inch = float(user)
# 계산
cm = inch * per_inch
# 결과를 표시한다
desc = "{0}인치 = {1}센치".format(inch, cm)
print(desc)

