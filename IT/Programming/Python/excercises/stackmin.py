class Stack:

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def empty(self):
        return len(self._data) == 0

class StackMin(Stack):

    def __init__(self):
        super().__init__()
        self._minStack = Stack()

    def peek(self):
        return super().peek()

    def get_minimum(self):
        return self._minStack.peek()

    def pop(self):
        deleted = super().pop()
        if deleted == self._minStack.peek():
            self._minStack.pop()
        return deleted

    def push(self, item):
        super().push(item)
        if self._minStack.empty() or self._minStack.peek() >= item:
            self._minStack.push(item)

    def empty(self):
        return super().empty()