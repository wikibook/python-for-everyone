# for와 동일한 역할을 하는 함수를 자작한다
def for_func(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            v = next(it)
            callback(v)
        except StopIteration:
            break

# 리스트의 내용을 화면에 모두 출력한다
nums = [1,2,3]
for_func(
    nums,                   # 리스트
    lambda i : print(i))    # 반복 처리

# 딕셔너리의 내용을 화면에 모두 출력한다
ages = {"Taro":20, "Jiro":15, "Saburo":18}
for_func(
    ages.items(),           # (키, 값) 형식의 튜플를 얻는다
    lambda n: print(n))     # 반복 처리


