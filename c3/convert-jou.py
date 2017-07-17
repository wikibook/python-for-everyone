# 조를 평방미터로 변환
def convert_jou(jou, unit="에도 방식"):
    if unit == "에도 방식":
        base = 0.88 * 1.76
    elif unit == "쿄토 방식":
        base = 0.955 * 1.91
    elif unit == "중경 방식":
        base == 0.91 * 1.82
    m2 = jou * base
    s = "{0}으로 {1}조는 {2}㎡입니다.".format(unit,jou,m2)
    print(s)

# 함수 실행
convert_jou(6, "에도 방식")# --- (*1)
convert_jou(6, "쿄토 방식")  # --- (*2)
convert_jou(6)          # --- (*3)

