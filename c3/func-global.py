
# 함수 바깥에서 value에 100을 대입
value = 100

def changeValue():
    # value를 전역으로 선언
    global value
    # 함수 안에서 value를 변경
    value = 20

changeValue();
print("value=",value) # <--- 그럼 이 변수에 어떤 값이 들어 있을까?



