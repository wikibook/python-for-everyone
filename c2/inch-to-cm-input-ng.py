# 입력을 받아서 인치를 센티미터로 변환한다
# 변환해야 하는 값
per_inch = 2.54
# 사용자로부터 입력을 받는다
inch = input("inch? ")
# 계산
cm = inch * per_inch
# 결과를 표시한다
desc = "{0}inch = {1}cm".format(inch, cm)
print(desc)

