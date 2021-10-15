# class LinkedList:
#     """
#     Put docstring here
#     """

#     def __init__(self):
#         # initialization here
#         pass

#     def some_method(self):
#         # method body here
#         pass
class Node:
    """
    A class representing a Node

    Attributes
    ----------


    Methods
    -------
    __init__(data, next_):
        the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the next_ 

    """

    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_


class LinkedList:
    """
    A class for creating instances of a Linked List.

    Data and other attributes defined here:

    head: Node | None

    Methods defined here

    insert(value: any)
    contains(value: any) -> bool
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        # print(self.head)
        """"
        Insert creates a Node with the value that was passed and adds
        it to the head of the linked list shifting all other values down

        arguments:
        value : any

        returns: None
        """
        # create new node

        self.head = Node(value, self.head)
        print(self.head.data)

    def includes(self, value):
        if self.head.data == value:
            return True
        else:
            return False

    def to_string(self):
        return (f"{ Node.data } -> { LinkedList } -> any -> NULL")


ehab = LinkedList()
ehab.insert(2)
print(ehab.includes(4))
print(ehab.to_string)
aseel = LinkedList()
aseel.insert(10)
print(aseel.includes(10))
print(aseel.to_string)
