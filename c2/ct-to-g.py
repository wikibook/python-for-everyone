# 캐럿을 그램으로 변환한다
# 변환 되는 쪽의 값
per_ct = 0.2
# 유저로부터 입력을 받는다
user = input("몇 캐럿입니까?")
# 부동소수점으로 변환한다
ct = float(user)
# 계산한다
g = ct * per_ct
# 결과를 표시한다
desc = "{0}캐럿 = {1}그램".format(ct, g)
print(desc)

