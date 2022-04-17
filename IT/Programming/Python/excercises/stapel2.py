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


class StackMin:
    def __init__(self):
        self.stapel = Stack()
        self.min_value = None

    def peek(self):
        return self.stapel.peek()

    def get_minimum(self):
        return self.min_value

    def pop(self):
        value = self.stapel.pop()

        if value == self.min_value:
            self.min_value = self.find_min()

        return value

    def push(self, item):
        self.stapel.push(item)
        if self.min_value is None or item < self.min_value:
            self.min_value = item

    # Deze methode gaat doorheen heel de stack en voegt elke item toe aan een
    # nieuwe stack. Terwijl houdt hij ook bij wat de kleinste waarde is. Na deze
    # operatie gaat de code doorheen de nieuwe stack en voegt het alles terug toe
    # aan de originele stack die ondertussen al leeg was.
    def find_min(self):
        minimum = None
        temp = Stack()

        while not self.stapel.empty():
            value = self.stapel.pop()
            temp.push(value)
            if minimum is None or value < minimum:
                minimum = value
        while not temp.empty():
            self.stapel.push(temp.pop())
        return minimum

    def empty(self):
        return self.stapel.empty()
