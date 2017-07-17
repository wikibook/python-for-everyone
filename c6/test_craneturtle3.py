import unittest, craneturtle

class TestCraneturtle3(unittest.TestCase):

    def setUp(self):
        # 전처리
        # 인스턴스를 미리 생성해둔다
        self.crane = craneturtle.Crane()
        self.turtle = craneturtle.Turtle()
        self.octopus = craneturtle.Octopus()
        self.squid  = craneturtle.Squid()

    def tearDown(self):
        # 후처리
        pass

    def test_legs(self):
        # 학과 거북이의 다리 개수를 확인한다
        self.assertEqual(self.crane.get_legs(), 2, "다리의 개수")
        self.assertEqual(self.turtle.get_legs(), 4, "다리의 개수")

    def test_basic(self):
        # 학거북산을 계산한다
        crane, turtle = craneturtle.calc_craneturtle(
            self.crane, self.turtle,
            heads=10, legs=28)
        # 결과를 검증한다
        self.assertEqual((crane,turtle),(6,4), "기본적인 계산")

    def test_crane_squid(self):
        # 검증
        self.assertEqual(
            craneturtle.calc_craneturtle(
                self.crane, self.squid,
                heads=6, legs=36),
            (3, 3), "학과 오징어를 계산")
