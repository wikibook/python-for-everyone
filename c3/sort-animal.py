# (동물, 최고 속도)로 구성된 리스트(각 요소는 튜플로 작성)
animal_list = [
    ("사자", 58),
    ("치타", 110),
    ("얼룩말", 60),
    ("순록", 80),
]

# 빠른 순서로 정렬한다
faster_list = sorted(
    animal_list, 
    key = lambda ani : ani[1], 
    reverse = True)

# 결과를 표시한다
for i in faster_list: print(i)

