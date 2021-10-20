# from linked_list.linked_list import LinkedList

# from linked_list.linked_list import Node, LinkedList
from code_challenges.cc5.linked_list import Node,  LinkedList
import pytest


# def test_version():
#     assert __version__ == '0.1.0'


def test_node_has_int_data():
    # Arrange any data that you need to run your test
    expected = 1

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.data

    # Assert
    assert actual == expected


def test_node_has_str_data():
    # Arrange any data that you need to run your test
    expected = "a"

    # Act on the subject of the test to produce some actual output
    node = Node("a")
    actual = node.data

    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange any data that you need to run your test
    expected = "Node"

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = type(node).__name__

    # Assert
    assert actual == expected


def test_node_without_value():
    with pytest.raises(TypeError):
        node = Node()


def test_new_linked_list_is_empty():
    # Arrange
    expected = None
    ll = LinkedList()
    # Act
    actual = ll.head
    # Assert
    assert actual == expected


def test_linked_list_insert():
    # Arrange
    expected = 1
    ll = LinkedList()

    # Act
    ll.insert(1)
    # node = ll.head
    actual = ll.head.data

    # Assert
    assert actual == expected


def test_linked_list_insert_twice():
    # Arrange
    expected = 0
    ll = LinkedList()

    # Act
    ll.insert(6)
    ll.insert(0)
    node = ll.head
    actual = node.data

    # Assert
    assert actual == expected
    assert ll.head.nxt.data == 6


def test_linked_inclue():
    # Arrange
    expected = True
    ll = LinkedList()
    # Act
    ll.insert(1)
    ll.insert(3)
    actual = ll.includes(3)
    # Assert
    assert actual == expected
    assert ll.includes(1) == True
    assert ll.includes(4) == False


def test_linked_to_string():
    # Arrange
    expected = "{ a } -> { b } -> { c } -> NULL"
    ll = LinkedList()
    # Act
    ll.insert("c")
    ll.insert("b")
    ll.insert("a")
    # Assert
    actual = ll.to_string()
    # Assert
    assert actual == expected


def test_empty_lists():
    # Arrange
    excepted = 'There is no lists to zip'
    # Act
    first_ll = LinkedList()
    second_ll = LinkedList()
    actual = zip_lists(first_ll, second_ll)
    # Assert
    assert excepted == actual


def test_first_list_empty():
    # Arrange
    excepted = "{ 1 } -> { 2 } -> { 3 } -> NULL"
    # Act
    first_ll = LinkedList()
    second_ll = LinkedList()
    second_ll.insert(1)
    second_ll.append(2)
    second_ll.append(3)
    actual = zip_lists(first_ll, second_ll)
    # Assert
    assert excepted == actual


def test_second_list_empty():
    # Arrange
    excepted = "{ 1 } -> { 2 } -> { 3 } -> NULL"
    # Act
    first_ll = LinkedList()
    second_ll = LinkedList()
    first_ll.insert(1)
    first_ll.append(2)
    first_ll.append(3)
    actual = zip_lists(first_ll, second_ll)
    # Assert
    assert excepted == actual


def test_diff_list_length():
    # Arrange
    excepted = "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> { 7 } -> NULL"
    # Act
    first_ll = LinkedList()
    first_ll.insert(3)
    first_ll.append(5)
    first_ll.append(7)
    first_ll.insert(1)

    second_ll = LinkedList()
    second_ll.insert(2)
    second_ll.append(4)
    second_ll.append(6)
    actual = zip_lists(first_ll, second_ll)
    # Assert
    assert excepted == actual


def test_happy_path():
    # Arrange
    excepted = "{ 2 } -> { 5 } -> { 9 } -> { 3 } -> { 4 } -> { 6 } -> NULL"
    # Act
    first_ll = LinkedList()
    first_ll.insert(2)
    first_ll.append(9)
    first_ll.append(4)
    second_ll = LinkedList()
    second_ll.insert(5)
    second_ll.append(3)
    second_ll.append(6)
    print(str(second_ll))
    actual = zip_lists(first_ll, second_ll)
    # Assert
    assert excepted == actual
