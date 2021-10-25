from stack_queue_pseudo.stack_queue_pseudo import Pseudo_queue


def test_input_multi():
    # Arrange
    expected = 2
    Pseudoqueue = Pseudo_queue()
    # Act
    Pseudoqueue.enqueue()
    Pseudoqueue.enqueue(1)
    Pseudoqueue.enqueue(2)
    actual = Pseudoqueue.rear
    # Assert
    assert expected == actual


def test_pseudo():
    # Arrange
    expected = 1
    Pseudoqueue = Pseudo_queue()
    # Act
    Pseudoqueue.enqueue(0)
    Pseudoqueue.enqueue(1)
    Pseudoqueue.dequeue()
    actual = Pseudoqueue.dequeue()
    # Assert
    assert expected == actual


def test_empty():
    # Arrange
    expected = None
    Pseudoqueue = Pseudo_queue()
    # Act
    actual = Pseudoqueue.dequeue()
    # Assert
    assert expected == actual
