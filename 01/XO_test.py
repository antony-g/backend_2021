import unittest
from XO import NewGame

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.gg = NewGame(3)

    def test_H(self):
        self.gg.move_test(0, 0)
        self.gg.move_test(0, 1)
        self.gg.move_test(0, 2)
        self.assertTrue(self.gg.check_win())

    def test_V(self):
        self.gg.move_test(0, 0)
        self.gg.move_test(1, 0)
        self.gg.move_test(2, 0)
        self.assertTrue(self.gg.check_win())

    def test_D(self):
        self.gg.move_test(0, 0)
        self.gg.move_test(1, 1)
        self.gg.move_test(2, 2)
        self.assertTrue(self.gg.check_win())


if __name__ == '__main__':
    unittest.main()
