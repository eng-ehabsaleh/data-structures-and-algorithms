class Node:
    def __init__(self, head, nxt=None):
        self.head = head
        self.nxt = nxt


class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.nxt = self.top
        self.top = node

    def pop(self):

        if self.top == None:
            raise EmptyStack("This stack is empty")

        temp = self.top
        self.top = self.top.nxt
        temp.nxt = None

        return temp.value

    def peek(self):

        return self.top.value

    def is_empty(self):

        return self.top == None


class Pseudo_queue:
    def __init__(self):
        self.instance1 = Stack()
        self.instance2 = Stack()
        self.rear = None
        self.front = None

    def enqueue(self, value):
        self.instance1.push(value)
        self.rear = self.instance1.top.head

    def dequeue(self):
        pass


ehab = Pseudo_queue()
ehab.enqueue(1)
print(ehab.rear)
ehab.enqueue(2)
print(ehab.rear)
print(ehab.rear)
