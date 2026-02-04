class Bag:
    class _Node:
        __slots__ = "_value", "_next"

        def __init__(self, value):
            self._value = value
            self._next = None

    def __init__(self):
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size 
    
    def __str__(self):
        values = []
        current = self._head
        while current is not None:
            values.append(str(current._value))
            current = current._next
        return f"[{', '.join(values)}]"
    
    def __iter__(self):
        current = self._head
        while current is not None:
            yield current._value
            current = current._next

    def add(self, value):
        new_node = self._Node(value)
        new_node._next = self._head
        self._head = new_node

        self._size += 1

    def remove(self, value):
        if self._head is None: 
            raise IndexError("Bag is empty")
        
        if self._head._value == value:
            self._head = self._head._next
            size -= 1
            return
    
        current = self._head
        while current._next is not None:
            if current._next._value == value:
                current._next = current._next._next
                self._size -= 1
                return
            current = current._next

        raise ValueError(f"{value} not found in bag")

    def clear(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0