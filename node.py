
from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None

    @staticmethod
    def _get_value(other):
        if isinstance(other, Node):
            return other.value
        else:
            return other

    def __int__(self):
        return int(self.value)

    def __str__(self) -> str:
        return str(self.value)

    def __add__(self, other):
        return self.value + self._get_value(other)

    def __sub__(self, other):
        return self.value - self._get_value(other)

    def __mul__(self, other):
        return self.value * self._get_value(other)

    def __truediv__(self, other):  # FIXME incorrect result when dividing multiple values at once
        return self.value / self._get_value(other)

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __rtruediv__ = __truediv__
