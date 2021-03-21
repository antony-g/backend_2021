"""Класс Список"""
import numbers


class MyList(list):
    """
    User-specified mutable sequence.

    If no argument is given, the constructor creates a new empty list.
    If arguments are given, the constructor creates a list of values. (NEW!)
    """

    def __init__(self, *args):
        super(MyList, self).__init__()
        if args is None:
            self.values = list()
        else:
            self.values = list(args)

    def __repr__(self):
        """ Return repr(self). """
        return str(self.values)

    def __add__(self, other):
        """ Return [self] || [other]. """
        if isinstance(other, MyList):
            return self.values + other.values
        elif isinstance(other, list):
            return self.values + other
        elif issubclass(int, numbers.Rational):
            # self.values.append(other)
            return list(self.values + [other])

    def __sub__(self, other):
        """ Return [self] && ![other]. """
        src = MyList()
        src = src + self.values
        for i in src:
            for j in other.values:
                if i is j:
                    src.remove(i)
        return src
        # [[0 if i is j else i & j for i in self.values] for j in other.values]

    def __mul__(self, other):
        """ Return [self] && [other]. """
        src = MyList()
        for i in self.values:
            for j in other.values:
                if i == j:
                    src.values.append(i)
        return src.values
        # return list({i if i is j else None for i in self.values for j in other.values})

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return -self.__sub__(other)

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

    def __neg__(self):
        """ Implement [self] *= -1. """
        return [-x for x in self.values]

    def __eq__(self, other):
        """ Return [self] == [other]. """
        return sorted(self.values) == sorted(other.values)

    def __ne__(self, other):
        """ Return [self] != [other]. """
        return sorted(self.values) != sorted(other.values)

    def __gt__(self, other):
        """ Return len([self]) > len([other]). """
        return len(self.values) > len(other.values)

    def __lt__(self, other):
        """ Return len([self]) < len([other]). """
        return len(self.values) < len(other.values)

    def __ge__(self, other):
        """ Return len([self]) >= len([other]). """
        return len(self.values) >= len(other.values) if len(self.values) != len(other.values) else sorted(
            self.values) == sorted(other.values)

    def __le__(self, other):
        """ Return len([self]) <= len([other]). """
        return len(self.values) <= len(other.values) if len(self.values) != len(other.values) else sorted(
            self.values) == sorted(other.values)

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
        self.values = sorted(self.values, key=key) if reverse is False else sorted(self.values, key=lambda x: -x)
        return self.values

    # def __repr__(self):
    #     """ Return repr(self). """
    #     return str(self.seq)

    # def __add__(self, other):
    #     """ Return self+value. """
    #     pass
    #
    # def __iadd__(self, other):
    #     """ Implement self+=value. """
    #     pass
    #
    # def __radd__(self, other):
    #     pass
    #
    # def __repr__(self):
    #     """ Return repr(self). """
    #     pass


if __name__ == '__main__':
    a = MyList(1, 2, 3)
    b = MyList(3, 4, 5)
    print(MyList(1, 2, 3))
    print(a + b)
    print(a + [4, 5, 6])
    print(a + 6)
    print(a - b)
    print(a * b)
    print(-a)
    a += 3
    print(a)
    b -= 3
    print(b)
    print(MyList(1, 2, 3) == MyList(3, 2, 1))
    print(MyList(1, 2) < MyList(1, 2, 3))
    print(MyList(1, 2, 3) > MyList(1, 2))
    print(a.__repr__())
    a.append(7)
    print(a)
    a.remove(5)
    print(a)
    a.sort(key=lambda x: -x)
    # a.sort(reverse=True)
    print(a)
    c = MyList(3, 2, 1)
    print(c)
    c.sort()
    print(c)
    # print(a.index(10))
