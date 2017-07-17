# 시급 계산 프로그램

# 시급을 입력 --- (*1)
user = input("시급은 얼마입니까?")
hourly_wage = int(user)

# 시간 입력
user = input("몇 시간 일했습니까?")
time = int(user)

# 계산 --- (*2)
total_wage = hourly_wage * time

# 결과 표시 --- (*3)
fmt = """
시급 {0}원으로 {1}시간 일했으므로...
수당은 {2}원입니다.
"""
desc = fmt.format(hourly_wage, time, total_wage)
print(desc)

