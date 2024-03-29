
from typing import Any

from .node import Node


class Linkedlist:
    def __init__(self, *args):
        self.head = None
        [self.append(i) for i in args]

    def append(self, value) -> None:
        if type(value) == Node:
            raise TypeError("Appending Node type not allowed")
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return None
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node
        return None

    def pop(self, index: int = None) -> None:
        curr_node = self.head
        if index is not None:
            if type(index) != int:
                raise TypeError("'{}' object is not iterable".format(type(index).__name__))
            if index == 0:
                self.head = self.head.next
                return None
            for j in range(index-1):
                if curr_node.next.next is None and index > j:
                    raise IndexError("Index out of range")
                else:
                    curr_node = curr_node.next
            curr_node.next = curr_node.next.next
        elif index is None:
            while curr_node.next.next is not None:
                curr_node = curr_node.next
            curr_node.next = curr_node.next.next
        return None

    def insert(self, index: int, value: Any) -> None:
        if type(value) == Node:
            raise TypeError("Inserting Node type not allowed")
        if index < 0:
            raise IndexError("Index out of range")
        curr_node = self.head
        for j in range(index-1):
            if curr_node.next is None and index > j:
                raise IndexError("Index out of range")
            else:
                curr_node = curr_node.next
        new_node = Node(value)
        new_node.next = curr_node.next
        curr_node.next = new_node
        return None

    def clear(self) -> None:
        next_node = self.head.next
        while next_node is not None:
            del self.head
            self.head = next_node
            next_node = next_node.next
        self.head = None
        return None

    def extend(self, values) -> None:
        for i in values:
            self.append(i)
        return None

    def __str__(self) -> str:
        result: str
        if self.head is None:
            result = "None"
        else:
            elements = []
            curr_node = self.head
            while curr_node is not None:
                elements.append(str(curr_node.value))
                curr_node = curr_node.next
            result = " -> ".join(elements) + " -> None"
        return result

    def __getitem__(self, index: int) -> Node:
        if index < 0 or self.head is None:
            raise IndexError("Index out of range")
        curr_node = self.head
        for j in range(index):
            if curr_node.next is None and index > j:
                raise IndexError("Index out of range")
            else:
                curr_node = curr_node.next
        return curr_node

    def __iter__(self) -> None:
        curr_node = self.head
        while curr_node is not None:
            yield curr_node.value
            curr_node = curr_node.next
        return None

    def __len__(self):
        curr_node = self.head
        count = 0
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next
        return count
