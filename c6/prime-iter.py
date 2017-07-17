# 소수를 열거하는 이터레이터 클래스
class PrimeIter:
    def __init__(self, max):
        """ 최대값을 지정한다 """
        self.max = max

    def __iter__(self):
        """ 값을 초기화한다 """
        self.n = 1 
        return self

    def __next__(self):
        """ 다음 소수를 찾아서 반환한다 """
        is_prime = False
        self.n += 1
        # 소수를 찾는다
        while not is_prime:
            is_prime = True
            for i in range(2, self.n):
                if self.n % i == 0:
                    is_prime = False
                    break
            if is_prime: break
            self.n += 1
            # 최대값에 도달하면 예외를 발생시킨다
            if self.n >= self.max:
                raise StopIteration
        return self.n

# 100 이하 소수를 열거한다
it = PrimeIter(100)
for no in it:
    print(no, end=",")
