# 동물의 최고속도 --- (*1)
animal_speed_dict = {
    "치타    ": 110, "순록    ": 80,
    "얼룩말  ": 60,  "사자    ": 58,
    "기린    ": 50,  "낙타    ": 30
}

# 토쿄에서 각 도시까지의 거리 --- (*2)
distance_dict = {
    "시즈오카": 183.7,
    "나고야  ": 350.6,
    "오오사카": 507.5
}

# 시간을 계산하는 함수 --- (*3)
def calc_time(dist, speed):
    t = dist / speed
    t = round(t, 1) # 반올림
    return t

# 각 도시까지 동물이 걸린 시간을 계산하는 함수 --- (*4)
def calc_animal(animal, speed):
    res = "|" + animal
    for city in sorted(distance_dict.keys()):
        dist = distance_dict[city]
        t = calc_time(dist, speed)
        res += "|{0:>8}".format(t)
    return res + "|"

# 표 헤더를 표시 --- (*5)
print("+--------+--------+--------+--------+")
print("|동물이름", end="")
for city in sorted(distance_dict.keys()):
    print("|" + city, end="")
print("|")
print("+--------+--------+--------+--------+")

# 각 동물에 대한 결과를 구한다 --- (*6)
for animal, speed in animal_speed_dict.items():
    s = calc_animal(animal, speed)
    print(s)
print("+--------+--------+--------+--------+")

