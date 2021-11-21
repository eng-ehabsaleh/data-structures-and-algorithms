from code_challenges.reverse_linked_list import reverse_list
from sort.sort.sort_insertion import insertion_sort

def test_import():
    assert reverse_list

######################################Sort test############################


def test_insertion():
    # arrange
    ehab_list = [8, 4, 23, 42, 16, 15]
    expected = [4, 8, 15, 16, 23, 42]
    actuaehab_list = insertion_sort(ehab_list)
    assert expected == actuaehab_list


def test_insertion_2():
    ehab_list = [20, 18, 12, 8, 5, -2]
    excepted = [-2, 5, 8, 12, 18, 20]
    actuaehab_list = insertion_sort(ehab_list)
    assert excepted == actuaehab_list


def test_insertion_3():
    ehab_list = [5, 12, 7, 5, 5, 7]
    excepted = [5, 5, 5, 7, 7, 12]
    actuaehab_list = insertion_sort(ehab_list)
    assert excepted == actuaehab_list


def test_insertion_4():
    ehab_list = [2, 3, 5, 7, 13, 11]
    excepted = [2, 3, 5, 7, 11, 13]
    actuaehab_list = insertion_sort(ehab_list)
    assert excepted == actuaehab_list
    
