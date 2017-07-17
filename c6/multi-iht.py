class A:
    def printA(self):
        print("A")

class B:
    def printB(self):
        print("B")

class C:
    def printC(self):
        print("C")

class D(A, B, C):
    def printD(self):
        print("D")
        
    def printAll(self):
        self.printA()
        self.printB()
        self.printC()
        self.printD()

obj = D()
obj.printA()
obj.printB()
obj.printC()
obj.printD()
obj.printAll()

