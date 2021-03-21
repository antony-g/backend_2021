"""Метакласс Custom"""
from abc import ABCMeta


class Custom(ABCMeta):
    @staticmethod
    def __new__(mcs, name, bases, classdict):
        name = "Custom{0}".format(name)
        classdict = {key if key[0:2] == "__"
                else "custom_{0}".format(key): value
                for key, value in classdict.items()}

        return super().__new__(mcs, name, bases, classdict)
