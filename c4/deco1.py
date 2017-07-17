# 데코레이터 함수를 정의한다
def show_func_name(func):
    def wrapper(*args, **kwargs):
        print("--- start: " + func.__name__)
        res = func(*args, **kwargs)
        print("--- end: " + func.__name__)
        return res
    return wrapper

# 데코레이터를 사용한다
@show_func_name
def proverb1():
    print("현자의 조용한 이야기는 ")
    print("우매한 사람들의 고함보다 잘 통한다.")

@show_func_name
def proverb2():
    print("열심히 구하는 자에게는 반드시 주어진다.")


proverb1()
proverb2()
