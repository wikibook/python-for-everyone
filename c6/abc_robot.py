# abc 모듈을 임포트한다
from abc import ABCMeta, abstractmethod

# 추상 기저 클래스를 정의한다
class MazeRobot(metaclass=ABCMeta):

    @abstractmethod
    def init_robot(self): pass

    @abstractmethod
    def choose_dir(self): pass
