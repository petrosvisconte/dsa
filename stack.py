class Stack:
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

    def push(self, value):
        new_node = self._Node(value)
        new_node._next = self._head
        self._head = new_node

        self._size += 1

    def pop(self):
        if self._head is None:
            raise IndexError("Stack is already empty")
        
        val = self._head._value
        self._head = self._head._next
        self._size -= 1
        return val

    def peek(self):
        if self._head is None:
            raise IndexError("Peek from empty stack")
        return self._head._value
            
    def clear(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

