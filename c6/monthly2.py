# 해당 월에 대응하는 한글을 반환하는 클래스를 정의한다
class Monthly:
    month = ["일월","이월","삼월","사월","오월","유월",
        "칠월","팔월","구월","시월","십일월","십이월"]
    def __getitem__(self, key):
        i = int(key)
        return self.month[i-1]
    def __setitem__(self,key,value):
        i = int(key)
        self.month[i-1] = value

# 첨자로 접근해본다
t = Monthly()
t[10] = "September"
print(t[10])
print(t[12])
