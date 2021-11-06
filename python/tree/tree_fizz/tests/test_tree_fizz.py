from tree_fizz import __version__
from tree_fizz.tree_fizz_buzz import fizz_buzz, helper, Node, binarytree, binarysearchtree


def test_version():
    assert __version__ == '0.1.0'


def test_fizz_buzz_1():
    x = binarysearchtree()
    x.add(15)
    x.add(12)
    x.add(20)
    expected = "Fizz Buzz"
    y = fizz_buzz(x)
    actual = y.root.value
    assert actual == expected


def test_fizz_buzz_2():
    x = binarysearchtree()
    x.add(15)
    x.add(11)
    x.add(20)
    expected = "11"
    y = fizz_buzz(x)
    actual = y.root.left.value
    assert actual == expected


def test_fizz_buzz_3():
    x = binarysearchtree()
    x.add(15)
    x.add(12)
    x.add(20)
    expected = "Fizz"
    y = fizz_buzz(x)
    actual = y.root.left.value
    assert actual == expected


def test_fizz_buzz_4():
    x = binarysearchtree()
    x.add(15)
    x.add(12)
    x.add(20)
    expected = "Buzz"
    y = fizz_buzz(x)
    actual = y.root.right.value
    assert actual == expected
