
class A:
    def print(self):
        print("A")

class AB:
    def print(self):
        print("AB")

class AC:
    def print(self):
        print("AC")

class D(AB, AC):
    pass

obj = D()
obj.print()

