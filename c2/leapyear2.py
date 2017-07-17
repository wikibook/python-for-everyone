year = int(input("서기 몇 년 ? "))

# 윤년 판정 --- (*1)
is_leap = False
if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

# 결과 표시
if is_leap:
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")

