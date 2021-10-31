from node import Node


class EmptyStack(Exception):
    pass


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
