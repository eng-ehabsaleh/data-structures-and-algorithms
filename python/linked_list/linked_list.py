class Node:
    """
    A class representing a Node

    Attributes
    ----------


    Methods
    -------
    __init__(data, nxt_):
        the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the nxt_

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
        """"
        Insert creates a Node with the value that was passed and adds
        it to the head of the linked list shifting all other values down

        arguments:
        value : any

        returns: None
        """

        self.head = Node(value, self.head)

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

    def kth_from_end(self, k):
        """
        Return the node’s value that is k places from the tail of the linked list.
        arguments
        K 
        returns: the value of the k places
        """

        current = self.head
        node_length = 1

        while current.nxt:
            node_length += 1
            current = current.nxt
        current = self.head

        if k < 0:
            return

        elif k >= node_length:
            return

        value = node_length-k-1
        for i in range(node_length):

            if i == value:

                return current.data

            current = current.nxt
