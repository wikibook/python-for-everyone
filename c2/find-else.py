# for 구문에 else를 사용할 경우
# 식재료 목록
foodstuff = ["Banana", "Mango", "Fish", "Carrot", "cabbage"]

# 망고가 들어 있는지 확인한다
for food in foodstuff:
    if food == "Mango":
        print("망고가 들어 있습니다.")
        break
else:
    print("없습니다.")

