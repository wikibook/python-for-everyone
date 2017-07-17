# 성적 데이터를 딕셔너리형으로 정의
records = { 
    'Tanaka':72, 'Yamada':65, 'Hirata':100, 
    'Akai':56, 'Fukuda':66, 'Sakai':80 }
# 합계를 구한다 --- (*1)
sum_v = 0
for v in records.values():
    sum_v += v
# 평균점을 계산해서 결과를 표시한다
ave_v = sum_v / len(records)
print("합계점:", sum_v)
print("평균점:", ave_v)

# 성적 데이터 목록과 평균점과의 차이를 표시한다 --- (*2)
fmt = "| {0:<7} | {1:>4} | {2:>5}"
print("| 이름    | 점수 | 차이")
for name, v in sorted(records.items()):
    # 평균점과의 차이를 구한다
    diff_v = v - ave_v 
    # 소수점 이하를 반올림한다 --- (*3)
    diff_v = round(diff_v, 1)
    # 형식에 맞춰 출력 --- (*4)
    print(fmt.format(name, v, diff_v))

