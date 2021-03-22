"""Класс Список. Unittest"""
import unittest
from list import MyList


class MyListOperatorTest(unittest.TestCase):
    "Class Docstring"

    def test_eq(self):
        "Docstring"
        self.assertTrue(MyList(1, 2, 3) == MyList(3, 2, 1))

    def test_ne(self):
        "Docstring"
        self.assertTrue(MyList(1, 2, 3) != MyList(4, 5, 6))

    def test_gt(self):
        "Docstring"
        self.assertTrue(MyList(1, 2, 3) > MyList(1, 2))

    def test_ge(self):
        "Docstring"
        self.assertTrue(MyList(1, 2, 3) >= MyList(4, 5))

    def test_add_1(self):
        "Docstring"
        i = MyList(1, 2, 3)
        j = MyList(4, 5, 6)
        k = i + j
        self.assertEqual(k, MyList(1, 2, 3, 4, 5, 6))

    def test_add_2(self):
        "Docstring"
        i = MyList(1, 2, 3)
        j = [4, 5, 6]
        k = i + j
        self.assertEqual(k, MyList(1, 2, 3, 4, 5, 6))

    def test_add_3(self):
        "Docstring"
        i = MyList(1, 2)
        j = 3
        k = i + j
        self.assertEqual(k, MyList(1, 2, 3))

    def test_sub_1(self):
        "Docstring"
        i = MyList(1, 2, 3)
        j = MyList(3, 4, 5)
        k = i - j
        self.assertEqual(k, MyList(1, 2))

    def test_sub_2(self):
        "Docstring"
        i = MyList(1, 2, 3)
        j = [3, 4, 5]
        k = i - j
        self.assertEqual(k, MyList(1, 2))

    def test_sub_3(self):
        "Docstring"
        i = MyList(1, 2, 3)
        j = 3
        k = i - j
        self.assertEqual(k, MyList(1, 2))

    def test_mul_1(self):
        "Docstring"
        i = MyList(1, 2, 3)
        j = MyList(3, 4, 5)
        k = i * j
        self.assertEqual(k, MyList(3))

    def test_mul_2(self):
        "Docstring"
        i = MyList(1, 2, 3)
        j = [3, 4, 5]
        k = i * j
        self.assertEqual(k, MyList(3))

    def test_mul_3(self):
        "Docstring"
        i = MyList(1, 2, 3)
        j = 3
        k = i * j
        self.assertEqual(k, MyList(3))

    def test_iadd(self):
        "Docstring"
        i = MyList(1, 2, 3)
        i += 3
        self.assertEqual(i, MyList(4, 5, 6))

    def test_isub(self):
        "Docstring"
        i = MyList(6, 5, 4)
        i -= 3
        self.assertEqual(i, MyList(3, 2, 1))

    def test_abs(self):
        "Docstring"
        i = MyList(1, -2, 3)
        j = abs(i)
        self.assertEqual(j, MyList(1, 2, 3))

    def test_neg(self):
        "Docstring"
        i = MyList(1, -2, 3)
        j = -i
        self.assertEqual(j, MyList(-1, 2, -3))


class MyListMethodTest(unittest.TestCase):
    "Class Docstring"

    def test_append(self):
        "Docstring"
        i = MyList(1, 2)
        i.append(3)
        j = MyList(1, 2, 3)
        self.assertEqual(i, j)

    def test_clear(self):
        "Docstring"
        i = MyList(1, 2, 3)
        i.clear()
        j = MyList()
        self.assertEqual(i, j)

    def test_copy(self):
        "Docstring"
        i = MyList(1, 2, 3)
        j = i.copy()
        self.assertTrue(i is not j)

    def test_count(self):
        "Docstring"
        i = MyList(0, 1, 1, 2, 3, 5, 8, 13)
        self.assertEqual(i.count(0), 1)
        self.assertEqual(i.count(1), 2)
        self.assertEqual(i.count(10), 0)

    def test_index(self):
        "Docstring"
        i = MyList(0, 1, 1, 2, 3, 5, 8, 13)
        self.assertEqual(i.index(0), 0)
        self.assertEqual(i.index(1), 1)
        with self.assertRaises(ValueError):
            i.index(10)

    def test_remove(self):
        "Docstring"
        i = MyList(0, 1, 1, 2, 3, 5, 8, 13)
        i.remove(1)
        j = MyList(0, 1, 2, 3, 5, 8, 13)
        self.assertEqual(i, j)

    def test_sort_1(self):
        "Docstring"
        i = MyList(8, 9, 10, 7, 6, 5, 0, 1, 2, 4, 3)
        i.sort()
        j = MyList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(i, j)

    def test_sort_2(self):
        "Docstring"
        i = MyList(8, 9, 10, 7, 6, 5, 0, 1, 2, 4, 3)
        i.sort(reverse=True)
        j = MyList(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
        self.assertEqual(i, j)

    def test_sort_3(self):
        "Docstring"
        i = MyList(8, 9, 10, 7, 6, 5, 0, 1, 2, 4, 3)
        i.sort(key=lambda x: -x)
        j = MyList(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
        self.assertEqual(i, j)


if __name__ == '__main__':
    unittest.main()
