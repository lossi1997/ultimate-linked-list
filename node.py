
from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None

    @staticmethod
    def _get_value(other) -> int:
        if isinstance(other, Node):
            return other.value
        else:
            return other

    def __int__(self) -> int:
        return int(self.value)

    def __str__(self) -> str:
        return str(self.value)

    def __sub__(self, other) -> int | float:
        return self.value - self._get_value(other)

    def __rsub__(self, other) -> int | float:
        return self._get_value(other) - self.value

    def __truediv__(self, other) -> float:
        return self.value / self._get_value(other)

    def __rtruediv__(self, other) -> float:
        return self._get_value(other) / self.value

    def __add__(self, other) -> int | float:
        return self.value + self._get_value(other)

    def __mul__(self, other) -> int | float:
        return self.value * self._get_value(other)

    __radd__ = __add__
    __rmul__ = __mul__
