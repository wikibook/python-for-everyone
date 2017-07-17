# 클래스를 설계한다
class Human:
    ''' 인간을 나타내는 클래스 '''
    
    def search(self, place):
        '''주위를 둘러보는 처리'''
        pass
      
    def take(self, food):
        '''물건을 집는 처리'''
        self.food = food
        
    def open_mouth(self):
        '''입을 여는 처리'''
        pass
        
    def eat(self):
        '''음식을 먹는 처리'''
        print(self.food+"을(를) 먹었습니다.")
