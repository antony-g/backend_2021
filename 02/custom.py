"""Метакласс Custom"""
from abc import ABCMeta


class Custom(ABCMeta):
    """Метакласс Custom"""
    @staticmethod
    def __new__(cls, *args, **kwargs):
        name = "Custom{0}".format(args[0])
        bases = args[1]
        class_dict = {key if key[:2] == "__"
                else "custom_{0}".format(key): value
                for key, value in args[2].items()}


        return super().__new__(cls, name, bases, class_dict)
