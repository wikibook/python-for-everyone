class Student:
    ''' 학생을 나타내는 클래스 '''
    def __init__(self, id, name, score = 0):
        ''' 초기화 '''
        self.id = id
        self.name = name
        self.score = score
        
    def getId(self):
        ''' ID를 얻어내는 메서드 '''
        return self.id
        
    def getName(self):
        ''' 학생 이름을 얻어내는 메서드 '''
        return self.name
        
    def setScore(self, score):
        ''' 점수를 얻어내는 클래스 '''
        self.score = score
        
    def getScore(self):
        ''' 점수를 저장하는 메서드 '''
        return self.score

class CalcScore:
    ''' 점수를 계산하는 함수 '''
    def __init__(self):
        ''' 초기화 '''
        self.students = []
        
    def addStudent(self, student):
        ''' 학생을 추가한다 '''
        self.students.append(student)

    def ave(self):
        v = 0
        for i in self.students:
            v += i.getScore()
        ave_v = v / len(self.students)
        return ave_v

# 학생 인스턴스를 생성
p1 = Student(10, "김")
p1.setScore(80)
p2 = Student(11, "이", score=79)
p3 = Student(12, "박", score=84)
p4 = Student(13, "최", score=77)

# 평균점수를 계산한다
calc = CalcScore()
calc.addStudent(p1)
calc.addStudent(p2)
calc.addStudent(p3)
calc.addStudent(p4)
print("평균점수=", calc.ave())
