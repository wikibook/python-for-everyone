# 가위바위보 게임
import random   # random 모듈을 가져온다

# 표현할 문자열 리스트
hand = ["바위", "가위", "보", "게임 종료"]

print("=== 가위바위보를 합시다！ ===")
while True:
    # 컴퓨터가 낼 것을 결정한다
    com = random.randint(0, 2)
    # 사용자가 낼 것을 입력을 받는다
    for i,desc in enumerate(hand):
        print(i, ":", desc)
    you = int(input("낼 것을 숫자로 입력: "))
    if you == 3: break
    if you < 0 or you > 2:
        print("0부터 3까지 숫자 중에 선택하세요.")
        continue
    # 화면에 표시한다
    print("---")
    print("나:", hand[you])
    print("상대:", hand[com])
    input("---")
    # 승패를 판정한다
    j = (you - com + 3) % 3
    if j == 0:
        print("비겼습니다.")
    elif j == 1:
        print("졌습니다.(ToT)")
    else:
        print("이겼습니다!!")
    input("---")



