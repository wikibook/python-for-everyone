# 동물 : 최고 속도를 딕셔너리로 표현했다
animal_dict = {
    "사자": 58,
    "치타": 110,
    "얼룩말": 60,
    "순록": 80
}

# 속도를 기준으로 정렬해서 표시한다
li = sorted(
    animal_dict.items(), 
    key=lambda x: x[1],
    reverse=True)
for name,speed in li:
    print(name, speed)

