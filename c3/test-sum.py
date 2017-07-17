# 어떤 학급의 국어 시험 점수를 리스트에 대입 --- (*1)
points = [88, 76, 67, 43, 79, 80, 91]

# 시험 합계를 구한다 --- (*2)
sum_v = 0
for i in points:
    sum_v += i
    print(i,"점을 더한 합계는 ", sum_v)

# 평균을 구한다 --- (*3)
ave_v = sum_v / len(points)
print("평균점은 ", ave_v, "점")

