
def test_duck(it):
    it.sound()
    it.walk()

class Empty: pass

monkey = Empty()
monkey.sound = lambda : print("끽끽")
monkey.walk = lambda : print("원숭이가 걸어간다.")

test_duck(monkey)


