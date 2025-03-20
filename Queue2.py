class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self):
        self.begin_of_queue = None
        self.end_of_queue = None

    def push_back(self, value):
        new_node = Node(value)
        if self.end_of_queue is None:
            self.begin_of_queue = self.end_of_queue = new_node
        else:
            self.end_of_queue.next = new_node
            new_node.prev = self.end_of_queue
            self.end_of_queue = new_node

    def pop_front(self):
        if self.begin_of_queue is None:
            raise IndexError("Queue is empty")
        removed_value = self.begin_of_queue.value
        self.begin_of_queue = self.begin_of_queue.prev
        if self.begin_of_queue is None:
            self.end_of_queue = None
        else:
            self.begin_of_queue.next = None
        return removed_value

    def empty(self):
        return self.begin_of_queue is None

    def front(self):
        if self.begin_of_queue is None:
            raise IndexError("Queue is empty")
        return self.begin_of_queue.value