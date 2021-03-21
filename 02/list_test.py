import unittest
from list import MyList


class MyListOperatorTest(unittest.TestCase):
    def test_eq(self):
        self.assertTrue(MyList(1, 2, 3) == MyList(3, 2, 1))

    def test_ne(self):
        self.assertTrue(MyList(1, 2, 3) != MyList(4, 5, 6))

    def test_gt(self):
        self.assertTrue(MyList(1, 2, 3) > MyList(1, 2))

    def test_ge_1(self):
        self.assertTrue(MyList(1, 2, 3) >= MyList(4, 5))

    def test_ge_2(self):
        self.assertTrue(MyList(1, 2, 3) >= MyList(4, 5, 6))
    # Assertion failed

    def test_add_1(self):
        x = MyList(1, 2, 3)
        y = MyList(4, 5, 6)
        z = MyList(x + y)
        self.assertTrue(z == MyList(1, 2, 3, 4, 5, 6))
    # Assertion failed

    def test_add_2(self):
        x = MyList(1, 2, 3)
        y = [4, 5, 6]
        z = MyList(x + y)
        self.assertTrue(z == MyList(1, 2, 3, 4, 5, 6))
    # Assertion failed

    def test_add_3(self):
        x = MyList(1, 2)
        y = 3
        z = MyList(x + y)
        self.assertTrue(z == MyList(1, 2, 3))
    # Assertion failed

    def test_sub_1(self):
        x = MyList(1, 2, 3)
        y = MyList(3, 4, 5)
        z = MyList(x - y)
        self.assertTrue(z == MyList(1, 2))
    # Assertion failed

    def test_sub_2(self):
        x = MyList(1, 2, 3)
        y = [3, 4, 5]
        z = MyList(x - y)
        self.assertTrue(z == MyList(1, 2))
    # Assertion failed

    def test_sub_3(self):
        x = MyList(1, 2, 3)
        y = 3
        z = MyList(x - y)
        self.assertTrue(z == MyList(1, 2))
    # Assertion failed

    def test_mul_1(self):
        x = MyList(1, 2, 3)
        y = MyList(3, 4, 5)
        z = MyList(x * y)
        self.assertTrue(z == MyList(3))
    # Assertion failed

    def test_mul_2(self):
        x = MyList(1, 2, 3)
        y = [3, 4, 5]
        z = MyList(x * y)
        self.assertTrue(z == MyList(3))
    # Assertion failed

    def test_mul_3(self):
        x = MyList(1, 2, 3)
        y = 3
        z = MyList(x * y)
        self.assertTrue(z == MyList(3))
    # Assertion failed

    def test_iadd(self):
        x = MyList(1, 2, 3)
        x += 3
        self.assertTrue(x == MyList(4, 5, 6))
    # Assertion failed

    def test_isub(self):
        x = MyList(6, 5, 4)
        x -= 3
        self.assertTrue(x == MyList(3, 2, 1))

class MyListMethodTest(unittest.TestCase):
    def test_append(self):
        x = MyList(1, 2)
        x.append(3)
        y = MyList(1, 2, 3)
        self.assertTrue(x == y)

    def test_clear(self):
        x = MyList(1, 2, 3)
        x.clear()
        y = MyList()
        self.assertTrue(x == y)

    def test_copy(self):
        x = MyList(1, 2, 3)
        y = x.copy()
        self.assertTrue(x is not y)

    def test_count(self):
        x = MyList(0, 1, 1, 2, 3, 5, 8, 13)
        self.assertEqual(x.count(0), 1)
        self.assertEqual(x.count(1), 2)
        self.assertEqual(x.count(10), 0)

    def test_index(self):
        x = MyList(0, 1, 1, 2, 3, 5, 8, 13)
        self.assertEqual(x.index(0), 0)
        self.assertEqual(x.index(1), 1)
        with self.assertRaises(ValueError):
            x.index(10)

    def test_remove(self):
        x = MyList(0, 1, 1, 2, 3, 5, 8, 13)
        x.remove(1)
        y = MyList(0, 1, 2, 3, 5, 8, 13)
        self.assertEqual(x, y)

    def test_sort_1(self):
        x = MyList(8, 9, 10, 7, 6, 5, 0, 1, 2, 4, 3)
        x.sort()
        y = MyList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(x, y)

    def test_sort_2(self):
        x = MyList(8, 9, 10, 7, 6, 5, 0, 1, 2, 4, 3)
        x.sort(reverse=True)
        y = MyList(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
        self.assertEqual(x, y)

    def test_sort_3(self):
        x = MyList(8, 9, 10, 7, 6, 5, 0, 1, 2, 4, 3)
        x.sort(key=lambda x: -x)
        y = MyList(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
        self.assertEqual(x, y)


if __name__ == '__main__':
    unittest.main()
