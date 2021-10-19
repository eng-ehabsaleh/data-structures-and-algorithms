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

    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt


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
        # print("before", self.head)
        self.head = Node(value, self.head)
        # self.ll.append(self.head)

        # print(self.head.nxt)
        # print("after1", self.head)
        # print("data", self.head.data)
        # print("next value", self.head.nxt)

    def includes(self, value):
        """insert function will loop through all the inside the dictionary(object)
                Arrgument
                Value:any
                returns :True/False"""
        element = self.head
        while element:
            if element.data == value:
                return True
            elif element.nxt is not None:
                element = element.nxt
            else:
                return False

    def to_string(self):
        """to_string function will loop trough all the dictionary (object) 
                Arrgument :no arrgument
                return all the data inside the dictionary"""

        string = ""
        element = self.head
        while element:
            string += "{ "+str(element.data)+" } -> "
            element = element.nxt
        string += "NULL"
        return string


# ehab = LinkedList()
# ehab.insert(2)
# ehab.insert(1)
# ehab.insert(6)
# print(ehab.to_string())
# print("for two", ehab.includes(2))
# print("for6", ehab.includes(6))
# print("for 3", ehab.includes(3))
# print("for 3", ehab.includes(3))
# print("for 3", ehab.includes(3))
