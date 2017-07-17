from abc_robot import MazeRobot

class MazeRobotTest(MazeRobot):
    
    def init_robot(self):
        print("로봇을 초기화합니다.")
    def choose_dir(self):
        print("전진합니다.")

robot = MazeRobotTest()
robot.init_robot()
