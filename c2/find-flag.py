# for 구문을 플래그를 사용하여 분기할 경우
# 식재료 목록
foodstuff = ["Banana", "Mango", "Fish", "Carrot", "cabbage"]

# 망고가 있는지 확인한다
flag_found = False
for food in foodstuff:
    if food == "Mango":
        flag_found = True
        break

if flag_found:
    print("망고가 들어 있습니다.")
else:
    print("없습니다.")


