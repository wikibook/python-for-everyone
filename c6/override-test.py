

class SuperClass:
    def blar(self):
        print("SuperClass.blar")

class SubClass(SuperClass):
    def blar(self):
        print("SubClass.blar")

it = SubClass()
it.blar()

