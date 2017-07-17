# 클래스를 정의한다
class HumanName:
    ''' 인간을 나타내는 클래스 '''
    def setName(self, name):
        ''' 이름을 설정하는 메서드 '''
        self.name = name
    
    def getName(self):
        ''' 이름을 얻어내는 클래스 '''
        return self.name

# 인스턴스를 생성한다
gildong = HumanName()
gildong.setName("Gildong")
print(gildong.getName())

chulsoo = HumanName()
chulsoo.setName("Chulsoo")
print(chulsoo.getName()) # --- (*1)
print(chulsoo.name)      # --- (*2)
