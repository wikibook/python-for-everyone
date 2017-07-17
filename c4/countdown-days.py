import datetime
# 다음 올림픽 개최일
t1 = datetime.date(2020, 7, 24)
# 오늘 날짜와의 차를 계산한다
t2 = datetime.date.today()
diff = t1 - t2
# 결과를 표시한다
print("오늘:", t2.strftime("%Y/%m/%d"))
print("다음 올림픽 개최일까지 ", diff.days, "일 남았습니다.")

