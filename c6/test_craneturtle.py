import unittest, craneturtle

class TestCraneturtle(unittest.TestCase):

    def test_craneturtle(self):
        # 학거북산을 계산한다
        crane, turtle = craneturtle.calc_craneturtle(
            craneturtle.Crane(),
            craneturtle.Turtle(), 
            heads=10, legs=28)

        # 결과를 검증한다
        self.assertEqual(crane, 6, "기본적인 계산을 통한 학의 수")
        self.assertEqual(turtle, 4, "기본적인 계산을 통한 거북이의 수")
