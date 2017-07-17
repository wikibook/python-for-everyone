s = input("체중을 입력: ")
try:
    v = 100 / float(s)
    print(v)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except:
    print("그밖의 오류")

