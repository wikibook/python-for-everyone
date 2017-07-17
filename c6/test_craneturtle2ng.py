import unittest, craneturtle

# 일부러 틀린 값은 지정한
class TestCraneturtle2(unittest.TestCase):

    def test_craneturtle_ng(self):
        # 학거북산을 계산한다
        crane, turtle = craneturtle.calc_craneturtle(
            craneturtle.Crane(),
            craneturtle.Turtle(), 
            heads=10, legs=28)

        # 결과를 검증한다
        self.assertEqual(crane, 8, "기본적인 계산을 통한 학의 수")
        self.assertEqual(turtle, 12, "기본적인 계산을 통한 거북이의 수")

