class LinkedList:
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

    def insert_beginning(self, value):
        new_node = self._Node(value)
        new_node._next = self._head
        self._head = new_node

        if self._tail is None:
            self._tail = new_node

        self._size += 1

    def insert_end(self, value):
        new_node = self._Node(value)
        if self._tail is None:
            self._tail = new_node
            self._head = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node
        
        self._size += 1

    def remove_beginning(self):
        if self._head is None:
            raise IndexError("Linked list is already empty")
        elif self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head._next
        
        self._size -= 1

    def remove_end(self):
        if self._tail is None:
            raise IndexError("Linked list is already empty")
        elif self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current._next is not self._tail:
                current = current._next
            self._tail = current
            self._tail._next = None

        self._size -= 1

    def remove(self, value):
        if self._head is None:
            raise IndexError("Linked list is empty")

        if self._head._value == value:
            self.remove_beginning()
            return

        current = self._head
        while current._next is not None:
            if current._next._value == value:
                if current._next is self._tail:
                    self.remove_end()
                else:
                    current._next = current._next._next
                    self._size -= 1
                return
            current = current._next

        raise ValueError(f"{value} not found in list")
    
    def find_node(self, value):
        if self._head is None:
            raise IndexError("Linked list is empty")
        
        current = self._head
        while current is not None:
            if current._value == value:
                return current
            current = current._next
        
        raise ValueError(f"{value} not found in list")
    
    def find(self, value):
        if self._head is None:
            raise IndexError("Linked list is empty")
        
        index = 0
        current = self._head
        while current is not None:
            if current._value == value:
                return index
            current = current._next
            index += 1
        
        raise ValueError(f"{value} not found in list")    
    
    def to_list(self):
        result = []
        current = self._head
        while current is not None:
            result.append(current._value)
            current = current._next
        return result

            
    def clear(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0
