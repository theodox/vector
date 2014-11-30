"""
Basic vector math for Maya.cmds

"""
from collections import namedtuple
import math


class Vector(object):
    """
    Generic vector operations.
    """

    def __add__(self, other):
        return type(self)(*(a + b for a, b in zip(self, other)))

    def __sub__(self, other):
        return type(self)(*(a - b for a, b in zip(self, other)))

    def __mul__(self, other):
        if hasattr(other, '__iter__'):
            return type(self)(*(a * b for a, b in zip(self, other)))
        return type(self)(*map(lambda a: a * other, self))

    def __div__(self, other):
        if hasattr(other, '__iter__'):
            return type(self)(*(a / b for a, b in zip(self, other)))
        return type(self)(*map(lambda a: a / other, self))

    def length(self):
        total = sum(map(lambda a: math.pow(a, 2), self))
        return math.sqrt(total)

    def normalized(self):
        divisor = [self.length()] * len(self)
        return type(self)(*(self / divisor))

    @classmethod
    def add(cls, a, b):
        return cls(*a) + cls(*b)

    @classmethod
    def sub(cls, a, b):
        return cls(*a) - cls(*b)

    @classmethod
    def mul(cls, a, b):
        return cls(*a) * cls(*b)

    @classmethod
    def div(cls, a, b):
        return cls(*a) / cls(*b)

    @classmethod
    def dot(cls, left, right):
        return sum(cls.mul(left, right))

    @classmethod
    def norm_dot(cls, left, right):
        left = cls(*left).normalized()
        right = cls(*right).normalized()

        return sum(cls.mul(left, right))


xy = namedtuple('Vector2', 'x y')
xyz = namedtuple('Vector3', 'x y z')
xyzw = namedtuple('Vector4', 'x y z w')


class Vector2(Vector, xy):
    """
    A 2-d xy vector.  This is an immutable tuple, so you cannot modify it in place!

    usage:

        v = Vector2 ( 1.0, 0.0)

    or
        example = [1.0., 0.0] # any iterable with 2 items
        v = Vector2(*example)

    or

       example = Vector2(x = 1.0, y=2.0)

    Supports all base iterable functions (slicing, for loops, any(), etc)
    """
    pass


class Vector3(Vector, xyz):
    """
    A 3-d xyz vector. This is an immutable tuple, so you cannot modify it in place!

    usage:

        v = Vector2 ( 1.0, 0.0, 0.0)

    or
        example = [1.0., 0.0, 0.0] # any iterable with 3 items
        v = Vector3(*example)

    or

       example = Vector3(x = 1.0, y=2.0, z = 3.0)

    Supports all base iterable functions (slicing, for loops, any(), etc)
    """
    pass


class Vector4(Vector, xyzw):
    """
    A 4-d xyzw vector. This is an immutable tuple, so you cannot modify it in place!

    usage:

        v = Vector2 ( 1.0, 0.0, 0.0, 1.0)

    or using *args:

        example = [1.0., 0.0, 0.0, 1.0] # any iterable with 4 items
        v = Vector4(*example)

    or explicitly

       example = Vector4(x = 1.0, y=2.0, z = 3.0, w= 0.0)

    Supports all base iterable functions (slicing, for loops, any(), etc)
    """
    pass


class MVector(Vector, list):
    """
    A mutable version of the base Vector. This allows you to modify vector contents in place.

    MVector derives from list so it supp


    Supports all base iterable functions (slicing, for loops, any(), etc). However it does NOT support append(), to keep the width of the vector to what it was at creation time.
    """

    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            args = args[0]
        list.__init__(self, args)
        for k in 'xyzw':
            if k in kwargs:
                self.__setattr__(k, kwargs.pop(k))

    def __getattr__(self, key):
        try:
            return self['xyzw'.index(key)]
        except KeyError:
            return self.__getattribute__(key)

    def __setattr__(self, key, value):
        if not key in 'xyzw':
            self.__setattribute__(key, value)
            return
        idx = 'xyzw'.index(key)
        self.__setitem__(idx, value)


    def __setitem__(self, key, value):
        while len(self) <= key:
            super(MVector, self).append(0.0)
        list.__setitem__(self, key, value)

    def append(self, *args):
        raise NotImplementedError(
            "MVector does not support appneding: create a new vector with the correct width instead")

