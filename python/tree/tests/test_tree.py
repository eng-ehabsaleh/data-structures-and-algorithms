from tree.tree import binarysearchtree
from tree import __version__


def test_version():
    assert __version__ == '0.1.0'


# first test "successfully instantiate an empty tree"
def test_empty_tree():
    tree = binarysearchtree()
    actual = tree.root
    expected = None
    assert actual == expected

# second test "successfully instantiate a tree with a single root node"


def test_single_root_node():
    ehab = binarysearchtree()
    ehab.add(1)
    ehab.add(2)
    ehab.add(3)
    ehab.add(4)
    actual = ehab.root.value
    expected = 1
    assert actual == expected

# third test "successfully add a left child and right child to a single root node"


def test_left_and_right_single_root_node():
    ehab = binarysearchtree()
    ehab.add(10)
    ehab.add(2)
    ehab.add(30)
    actual = (ehab.root.left.value, ehab.root.right.value)
    expected = (2, 30)
    assert actual == expected

# fourth test "successfully return a collection from an inorder traversal"


def test_inorder_traversal():
    ehab = binarysearchtree()
    ehab.add(1)
    ehab.add(5)
    ehab.add(2)
    ehab.add(7)
    ehab.add(11)
    ehab.add(3)
    actual = ehab.inorder()
    expected = [1, 2, 3, 5, 7, 11]
    assert actual == expected

# fifth test "successfully return a collection from a preorder traversal"


def test_preorder_traversal():
    ehab = binarysearchtree()
    ehab.add(1)
    ehab.add(5)
    ehab.add(2)
    ehab.add(7)
    ehab.add(11)
    ehab.add(3)
    actual = ehab.preorder()
    expected = [1, 5, 2, 3, 7, 11]
    assert actual == expected

# sixth test "successfully return a collection from a postorder traversal"


def test_postorder_traversal():
    ehab = binarysearchtree()
    ehab.add(1)
    ehab.add(5)
    ehab.add(2)
    ehab.add(7)
    ehab.add(11)
    ehab.add(3)
    actual = ehab.postorder()
    expected = [3, 2, 11, 7, 5, 1]
    assert actual == expected

# extra test "successfully return the value "dose not exist" in the tree "


def test_value_dne():
    ehab = binarysearchtree()
    ehab.add(1)
    ehab.add(5)
    ehab.add(2)
    ehab.add(7)
    ehab.add(11)
    ehab.add(3)
    actual = ehab.Contains(4)
    expected = "dose not exist"
    assert actual == expected

# extra test "successfully return if the valeu exist in the tree "


def test_value_exist():
    ehab = binarysearchtree()
    ehab.add(1)
    ehab.add(5)
    ehab.add(2)
    ehab.add(7)
    ehab.add(11)
    ehab.add(3)
    actual = ehab.Contains(11)
    expected = "the value is exist"
    assert actual == expected


def test_value_max_1():
    tree = binarysearchtree()
    tree.add(1)
    tree.add(5)
    tree.add(2)
    tree.add(7)
    tree.add(11)
    tree.add(3)
    actual = tree.max_value()
    expected = 11
    assert actual == expected

#   to return the max value of binary tree


def test_value_max_2():
    tree = binarysearchtree()
    tree.add(5)
    tree.add(2)
    tree.add(7)
    tree.add(3)
    actual = tree.max_value()
    expected = 7
    assert actual == expected
#   to return the max value of binary tree when its empty


def test_value_max_3():
    tree = binarysearchtree()
    actual = tree.max_value()
    expected = "empty tree"
    assert actual == expected
