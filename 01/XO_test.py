"""Игра крестики-нолики. Unittest"""

import unittest
from XO import NewGame


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.game = NewGame(3)

    def test_horizontal_win(self):
        self.game.move_test(0, 0)
        self.game.move_test(0, 1)
        self.game.move_test(0, 2)
        self.assertTrue(self.game.check_win())

    def test_vertical_win(self):
        self.game.move_test(0, 0)
        self.game.move_test(1, 0)
        self.game.move_test(2, 0)
        self.assertTrue(self.game.check_win())

    def test_diagonal_win(self):
        self.game.move_test(0, 0)
        self.game.move_test(1, 1)
        self.game.move_test(2, 2)
        self.assertTrue(self.game.check_win())

    def test_check_input_valid(self):
        self.assertRaises(IndexError, NewGame.move_test, self.game, 0, 3)

    def test_check_input_duplicate(self):
        self.game.move_test(0, 0)
        self.assertRaises(IndexError, NewGame.move_test, self.game, 0, 0)


if __name__ == '__main__':
    unittest.main()
