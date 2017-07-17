# 국어 시험 점수 목록 --- (*1)
points = [80, 40, 23, 14, 29, 58]

# 30점 이하의 데이터만을 선택해서 낮은 점수 리스트에 추가 --- (*2)
lowscore = []
for p in points:
    if p < 30:
        lowscore.append(p)

# 선택한 데이터를 표시 --- (*3)
print(lowscore)

