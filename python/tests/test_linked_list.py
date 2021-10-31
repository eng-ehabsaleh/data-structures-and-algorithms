
from linked_list.linked_list import Node,  LinkedList
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


def test_linked_include():
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


def test_linked_list_append():
    # Arrange
    expected = "{ a } -> { b } -> { c } -> { A } -> NULL"
    ll = LinkedList()
    # Act
    ll.insert("c")
    ll.insert("b")
    ll.insert("a")
    ll.append("A")
    actual = ll.to_string()
    # Assert
    assert actual == expected


def test_append_multie_nodes():
    # Arrange
    expected = "{ 1 } -> { 5 } -> { 6 } -> NULL"
    # Act
    ll = LinkedList()
    # Assert
    ll.insert(1)
    ll.append(5)
    ll.append(6)
    actual = ll.to_string()
    # Assert
    assert actual == expected


def test_insert_after_middle():
    ll = LinkedList()
    ll.insert(7)
    ll.insert(4)
    ll.insert(1)
    ll.append(74)
    ll.append(66)
    ll.insert_after(7, 5)
    ll.to_string()
    assert ll.to_string(
    ) == "{ 1 } -> { 4 } -> { 5 } -> { 7 } -> { 74 } -> { 66 } -> NULL"


def test_insert_before_middle():
    ll = LinkedList()
    ll.insert(7)
    ll.insert(4)
    ll.insert(1)
    ll.append(74)
    ll.append(66)
    ll.insert_before(7, 9)
    ll.to_string()
    assert ll.to_string(
    ) == "{ 1 } -> { 4 } -> { 7 } -> { 9 } -> { 74 } -> { 66 } -> NULL"


def test_insert_before_empty_list():
    # Arrange
    expected = "NULL"
    # Act
    ll = LinkedList()
    # Assert
    ll.insert_before(5, 1)
    actual = ll.to_string()
    # Assert
    assert actual == expected


def test_insert_after_first():
    ll = LinkedList()
    ll.insert(7)
    ll.insert(4)
    ll.insert(1)
    ll.append(74)
    ll.append(66)
    ll.insert_after(1, 100)
    ll.to_string()
    assert ll.to_string(
    ) == "{ 100 } -> { 1 } -> { 4 } -> { 7 } -> { 74 } -> { 66 } -> NULL"


def test_insert_before_middle():
    ll = LinkedList()
    ll.insert(7)
    ll.insert(4)
    ll.insert(1)
    ll.append(74)
    ll.append(66)
    ll.insert_before(7, 9)
    ll.to_string()
    assert ll.to_string(
    ) == "{ 1 } -> { 4 } -> { 7 } -> { 9 } -> { 74 } -> { 66 } -> NULL"


def test_insert_before_end():
    ll = LinkedList()
    ll.insert(7)
    ll.insert(4)
    ll.insert(1)
    ll.append(74)
    ll.append(66)
    ll.insert_before(66, 8)
    ll.to_string()
    assert ll.to_string(
    ) == "{ 1 } -> { 4 } -> { 7 } -> { 74 } -> { 66 } -> { 8 } -> NULL"
