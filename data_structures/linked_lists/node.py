class Node:
    __slots__ = ['_element', '_next']

    def __init__(self, element, next) -> None:
        self._element = element
        self._next = next
