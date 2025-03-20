class Queue:
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity
        self.array = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def _resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity

        for i in range(self.count):
            new_array[i] = self.array[(self.front + i) % self.capacity]

        self.array = new_array
        self.front = 0
        self.rear = self.count
        self.capacity = new_capacity

    def push(self, item):
        if self.count == self.capacity:
            self._resize()
        self.array[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise IndexError("Queue is empty")
        value = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value

    def peek(self):
        if self.count == 0:
            raise IndexError("Queue is empty")
        return self.array[self.front]

    def empty(self):
        return self.count == 0

    def size(self):
        return self.count

