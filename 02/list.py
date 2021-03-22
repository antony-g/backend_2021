"""Класс Список"""
import numbers
from collections.abc import Iterable


def flatten(values):
    """ Returns flatten values always as a list of depth 1. """
    for item in values:
        if isinstance(item, Iterable):
            for i in flatten(item):
                yield i
        else:
            yield item


class MyList(list):
    """
    User-specified mutable sequence.

    If no argument is given, the constructor creates a new empty list.
    If arguments are given, the constructor creates a list of values. (NEW!)
    """

    def __init__(self, *args):
        """ Init an instance of class. """
        super().__init__()
        if args is None:
            self.values = list()
        else:
            self.values = list(flatten(args))

    def __repr__(self):
        """ Return repr(self). """
        return str(self.values)

    def __add__(self, other):
        """ Return [self] || [other]. """
        if isinstance(other, MyList):
            return self.values + other.values
        elif isinstance(other, list):
            return self.values + other
        elif isinstance(other, numbers.Rational):
            return MyList(self.values + [other])
        else:
            return MyList(self.values + other)

    def __sub__(self, other):
        """ Return [self] && ![other]. """
        src = MyList()
        src = src + self.values
        for i in src:
            if isinstance(other, MyList):
                for j in other.values:
                    if i is j:
                        src.remove(i)
            elif isinstance(other, list):
                for j in other:
                    if i is j:
                        src.remove(i)
            elif isinstance(other, numbers.Rational):
                if other in src:
                    src.remove(other)
        return src

    def __mul__(self, other):
        """ Return [self] && [other]. """
        src = MyList()
        for i in self.values:
            if isinstance(other, MyList):
                for j in other.values:
                    if i is j:
                        src.values.append(i)
            elif isinstance(other, list):
                for j in other:
                    if i is j:
                        src.values.append(i)
            elif isinstance(other, numbers.Rational):
                if i == other:
                    src.values.append(i)
        return src.values

    def __radd__(self, other):
        """ Implement [self] || [other] for objects with no implemented method. """
        return self.__add__(other)

    def __rsub__(self, other):
        """ Implement [self] && ![other] for objects with no implemented method. """
        return self.__sub__(other)

    def __iadd__(self, other):
        """ Implement [self] += value. """
        for i in range(len(self.values)):
            self.values[i] += other
        return self.values

    def __isub__(self, other):
        """ Implement [self] -= value. """
        for i in range(len(self.values)):
            self.values[i] -= other
        return self.values

    def __abs__(self):
        """ Implement abs([self]). """
        return [x if x > 0 else -x for x in self.values]

    def __neg__(self):
        """ Implement [self] *= -1. """
        return [-x for x in self.values]

    def __eq__(self, other):
        """ Return [self] == [other]. """
        x_val = sorted(self.values)
        x_size = len(self.values)
        if isinstance(other, MyList):
            y_val = sorted(other.values)
            y_size = len(other.values)
        else:
            y_val = sorted(other)
            y_size = len(other)
        res = True
        if x_size == y_size:
            for i in range(x_size):
                if x_val[i] != y_val[i]:
                    res = False
                    break
        else:
            res = False
        return res

    def __ne__(self, other):
        """ Return [self] != [other]. """
        return not self.values == other.values

    def __gt__(self, other):
        """ Return len([self]) > len([other]). """
        return len(self.values) > len(other.values)

    def __lt__(self, other):
        """ Return len([self]) < len([other]). """
        return len(self.values) < len(other.values)

    def __ge__(self, other):
        """ Return len([self]) >= len([other]). """
        return len(self.values) > len(other.values)\
            if len(self.values) != len(other.values)\
            else sorted(self.values) == sorted(other.values)

    def __le__(self, other):
        """ Return len([self]) <= len([other]). """
        return len(self.values) < len(other.values)\
            if len(self.values) != len(other.values)\
            else sorted(self.values) == sorted(other.values)

    def append(self, *args):
        """ Append object to the end of the list. """
        self.values.append(*args)

    def clear(self):
        """ Remove all items from list. """
        self.values = []

    def count(self, value):
        """ Return number of occurrences of value. """
        res = 0
        for i in self.values:
            if i == value:
                res += 1
        return res

    def index(self, value):
        """ Return first index of value or raise ValueError. """
        res = 0
        for i in self.values:
            if i == value:
                break
            else:
                res += 1
        else:
            raise ValueError
        return res

    def remove(self, value):
        """ Return first occurrence of value or raise ValueError. """
        self.values.remove(value)
        return self.values

    def sort(self, key=None, reverse=False):
        """ Sort the list in ascending order and return None.
        The reverse flag can be set to sort in descending order. """
        self.values = sorted(self.values, key=key)\
            if reverse is False\
            else sorted(self.values, key=lambda x: -x)
        return self.values
