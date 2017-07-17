class Human:
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
        '''과일을 먹는 처리'''
        print(self.food+"를 먹었습니다.")

hito = Human()
hito.take("Banana")
hito.eat()

