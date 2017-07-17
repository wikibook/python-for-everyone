# 평수를 반복해서 알아보는 프로그램
while True:
    user = input("평수는? ")            #
    if user == "" or user == "q": break # 수정한 부분
    pyeong = int(user)                    #
    m2 = pyeong * 3.31
    s = "{0}평은 {1}제곱미터입니다.".format(pyeong, m2)
    print(s)

