"""Игра крестики-нолики. Unittest"""

import unittest
from XO import NewGame


class MyTestCase(unittest.TestCase):
    """Testing the game"""
    def setUp(self):
        """Start the Game"""
        self.game = NewGame(3)

    def test_show_board(self):
        """Testing initial board rendering"""
        self.game.show_board()
        self.assertEqual([[-1] * 3]*3, self.game._NewGame__field)

    def test_check_validate_input_1(self):
        """Testing regular input"""
        self.assertEqual(self.game.validate_input("a1"), (0, 0))

    def test_check_validate_input_2(self):
        """Testing input outside of the board"""
        self.assertEqual(self.game.validate_input("a4"), (0, 3))

    def test_check_validate_input_3(self):
        """Testing input outside of the board"""
        self.assertEqual(self.game.validate_input("h8"), (7, 7))

    def test_move_1(self):
        """Testing move of the 'O' player"""
        self.game.move(0, 0)
        self.assertEqual(self.game._NewGame__field[0][0], 0)

    def test_move_2(self):
        """Testing move of the 'X' player"""
        self.game.move(0, 0)
        self.game.move(0, 1)
        self.assertEqual(self.game._NewGame__field[1][0], 1)

    def test_move_3(self):
        """Outside of the board"""
        self.game.move(0, 3)

    def test_move_4(self):
        """Duplicated move"""
        self.game.move(0, 0)
        self.game.move(0, 0)

    def test_horizontal_win(self):
        """Testing each of 3 horizontal lines"""
        for i in range(3):
            self.game.move(i, 0)
            self.game.change_side()
            self.game.move(i, 1)
            self.game.change_side()
            self.game.move(i, 2)
            self.assertTrue(self.game.check_win())

    def test_vertical_win(self):
        """Testing each of 3 vertical lines"""
        for i in range(3):
            self.game.move(0, i)
            self.game.change_side()
            self.game.move(1, i)
            self.game.change_side()
            self.game.move(2, i)
            self.assertTrue(self.game.check_win())

    def test_diagonal_win_1(self):
        """Testing first diagonal line"""
        self.game.move(0, 0)
        self.game.change_side()
        self.game.move(1, 1)
        self.game.change_side()
        self.game.move(2, 2)
        self.assertTrue(self.game.check_win())

    def test_diagonal_win_2(self):
        """Testing second diagonal line"""
        self.game.move(2, 2)
        self.game.change_side()
        self.game.move(1, 1)
        self.game.change_side()
        self.game.move(0, 0)
        self.assertTrue(self.game.check_win())

    def test_draw(self):
        """Testing draw, winner is undecided"""
        self.game.move(0, 0)
        self.game.move(1, 1)
        self.game.move(0, 0)
        self.assertFalse(self.game.check_win())


if __name__ == '__main__':
    unittest.main()
