"""Игра крестики-нолики. Unittest"""

import unittest
from XO import NewGame

class MyTestCase(unittest.TestCase):
    "Docstring"
    def setUp(self):
        "Docstring"
        self.gg = NewGame(3)

    def test_h(self):
        "Docstring"
        self.gg.move_test(0, 0)
        self.gg.move_test(0, 1)
        self.gg.move_test(0, 2)
        self.assertTrue(self.gg.check_win())

    def test_v(self):
        "Docstring"
        self.gg.move_test(0, 0)
        self.gg.move_test(1, 0)
        self.gg.move_test(2, 0)
        self.assertTrue(self.gg.check_win())

    def test_d(self):
        "Docstring"
        self.gg.move_test(0, 0)
        self.gg.move_test(1, 1)
        self.gg.move_test(2, 2)
        self.assertTrue(self.gg.check_win())


if __name__ == '__main__':
    unittest.main()
