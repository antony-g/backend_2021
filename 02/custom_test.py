"""Метакласс Custom. Unittest"""
import unittest
from custom import Custom


class TestClass(metaclass=Custom):
    """Some_text"""
    some_variable = None

    def some_func(self):
        "Some func"
        return self.some_variable

    def some_func_2(self):
        "Empty func"


class VarNameTest(unittest.TestCase):
    """Testing class variable naming"""
    def test_positive(self):
        "Docstring"
        self.assertTrue(hasattr(TestClass, 'custom_some_variable'))

    def test_negative(self):
        "Docstring"
        self.assertFalse(hasattr(TestClass, 'some_variable'))


class MethodNameTest(unittest.TestCase):
    """Testing class methods naming"""
    def test_positive(self):
        "Docstring"
        self.assertTrue(hasattr(TestClass, 'custom_some_func'))

    def test_negative(self):
        "Docstring"
        self.assertFalse(hasattr(TestClass, 'some_func'))


class BuiltinNameTest(unittest.TestCase):
    """Testing built-in (magic) methods naming"""
    def test_positive(self):
        "Docstring"
        self.assertTrue(hasattr(TestClass, '__doc__'))

    def test_negative(self):
        "Docstring"
        self.assertFalse(hasattr(TestClass, 'custom__doc__'))


class ClassNameTest(unittest.TestCase):
    """Testing class naming"""
    def test_positive(self):
        "Docstring"
        self.assertEqual(TestClass.__name__, 'CustomTestClass')

    def test_negative(self):
        "Docstring"
        self.assertNotEqual(TestClass.__name__, 'TestClass')


if __name__ == '__main__':
    unittest.main()
