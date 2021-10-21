from stack_and_queue.node import Node
from stack_and_queue.queue import Queue
from stack_and_queue.stack import Stack


def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("Python")
    actual = queue.rear.value
    expected = "Python"
    assert actual == expected


def test_is_empty():
    queue = Queue()
    assert queue.is_empty() == True
    # assert queue.is_empty()


def test_is_empty(stack):
    stack = Stack()
    assert stack.is_empty() == True


def test_peek(stack):
    stack = Stack()
    actual = stack.peek()
    expected = 'Python'
    assert actual == expected
