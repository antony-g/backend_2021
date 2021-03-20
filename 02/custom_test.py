import unittest
from custom import Custom


class TestClass(metaclass=Custom):
    """Some_text"""
    some_variable = None

    def some_method(self):
        return self.some_variable


class VarNameTest(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(hasattr(TestClass, 'custom_some_variable'))

    def test_negative(self):
        self.assertFalse(hasattr(TestClass, 'some_variable'))


class MethodNameTest(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(hasattr(TestClass, 'custom_some_method'))

    def test_negative(self):
        self.assertFalse(hasattr(TestClass, 'some_method'))


class ClassNameTest(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(TestClass.__name__, 'CustomTestClass')

    def test_negative(self):
        self.assertNotEqual(TestClass.__name__, 'TestClass')


class BuiltinNameTest(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(hasattr(TestClass, '__doc__'))

    def test_negative(self):
        self.assertFalse(hasattr(TestClass, 'custom__doc__'))


if __name__ == '__main__':
    unittest.main()
