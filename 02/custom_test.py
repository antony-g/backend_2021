"""Метакласс Custom. Unittest"""
import unittest
from custom import Custom


class TestClass(metaclass=Custom):
    """Some_text"""
    some_variable = None

    def some_func(self):
        """Some func"""
        return self.some_variable

    def some_func_2(self):
        """Some empty func"""


class MyTestCase(unittest.TestCase):
    """Testing class variable naming"""
    def test_var(self):
        self.assertTrue(hasattr(TestClass, 'custom_some_variable'))

    def test_method(self):
        self.assertTrue(hasattr(TestClass, 'custom_some_func'))

    def test_builtin(self):
        self.assertTrue(hasattr(TestClass, '__doc__'))

    def test_class(self):
        self.assertEqual(TestClass.__name__, 'CustomTestClass')


if __name__ == '__main__':
    unittest.main()
