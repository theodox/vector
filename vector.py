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
    """
    pass