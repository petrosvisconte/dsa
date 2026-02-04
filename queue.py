class Queue:
    class _Node:
        __slots__ = "_value", "_next"

        def __init__(self, value):
            self._value = value
            self._next = None

    def __init__(self):
        self._head = None
        self._tail = None
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

    def enqueue(self, value):
        new_node = self._Node(value)
        if self._tail is None:
            self._tail = new_node
            self._head = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node
        
        self._size += 1

    def dequeue(self):
        if self._head is None:
            raise IndexError("Queue is already empty")
        
        val = self._head._value
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head._next
        
        self._size -= 1
        return val
    
    def peek(self):
        if self._head is None:
            raise IndexError("Peek from empty queue")
        return self._head._value
            
    def clear(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0