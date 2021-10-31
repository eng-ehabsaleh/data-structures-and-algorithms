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

    def append(self, new_value):
        """ function will add the given value as a node to the end of the list
        argument
        new _value
        return none"""
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node

            return

        last = self.head
        while (last.nxt):
            last = last.nxt
        last.nxt = new_node

    def insert_before(self, pre, new):
        """
        function will add a new node before the given value
        arguments
        new
        pre
        returns none
        """

        new_node = Node(new)
        current_value = self.head
        while current_value:
            if current_value.data == pre:
                new_node.nxt = current_value.nxt
                current_value.nxt = new_node
                break
            current_value = current_value.nxt

    def insert_after(self, pre, new):
        """
        function will add a new value as a node after the given value
        arguments
        new
        after
        returns null if the linked list is empty
        """

        node = Node(new)
        current_value_node = self.head
        if current_value_node.data == pre:
            node.nxt = self.head
            self.head = node
        else:
            while current_value_node.nxt:
                if current_value_node.nxt.data == pre:
                    node.nxt = current_value_node.nxt
                    current_value_node.nxt = node
                    break
                current_value_node = current_value_node.nxt


ehab = LinkedList()
ehab.insert(2)
ehab.insert(1)
ehab.insert(6)
ehab.append(3)

ehab.insert_before(2, 8)
ehab.insert_after(2, 7)
print(ehab.to_string())
