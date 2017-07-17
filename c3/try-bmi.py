# BMI 판정(예외 처리가 있는 버전)
# 사용자로부터 옳은 값을 받아서 BMI를 계산한다
while True:
    try:
        # 입력
        weight = float(input("체중(kg)은 ? "))
        height = float(input("키(cm)는 ? "))
        # BMI를 계산한다I
        height = height / 100 # m으로 고친다
        bmi = weight / (height * height)
        break;
    except:
        print("입력한 값에 문제가 있습니다. 다시 입력해주세요.")

# bmi 값을 가지고 결과를 판정한다
result = ""
if bmi < 18.5: result = "마른 체형"
elif bmi < 25: result = "표준 체중"
elif bmi < 30: result = "비만(경도)"
else: result = "비만(심각)"

# 결과를 표시한다
print("BMI :", bmi)
print("판정:", result)

