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

    def zip_lists(list1, list2):
        """function takes two lists as argument and return one list which is result of alternate between the two lists and return a reference to the head of the zipped list."""

        first = list1.head
        second = list2.head

        if not first and not second:

            return 'There is no lists to zip'

        elif not first:

            return str(list2)

        elif not second:
            return str(list1)

        fixed_node = ''

        while first and second:
            if second:
                fixed_node = first.nxt
                first.nxt = second
                first = fixed_node

            if first:
                fixed_node = second.nxt
                second.nxt = first
                second = fixed_node

        return str(list1)

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

    def insert_before(self, new, pre):
        """
        function will add a new node before the given value
        arguments
        new 
        pre 
        returns none
        """

        current = self.head
        if not current:
            return "NULL"
        while current.nxt:
            if current.nxt.data == pre:
                new_node = Node(new)
                new_node.nxt = current.nxt
                current.nxt = new_node
        current = current.nxt

    def insert_after(self, new, after):
        """
        function will add a new value as a node after the given value
        arguments
        new 
        after 
        returns null if the linked list is empty 
        """

        current = self.head
        if not current.nxt:
            return "This the linked list tile"
        while current.nxt:
            if current.data == after:
                new_node = Node(new)
                new_node.nxt = current.nxt
                current.nxt = new_node
        current = current.nxt


ehab = LinkedList()
ehab.insert(2)
ehab.insert(1)
ehab.insert(6)
# ehab.insert_before(2, 6)
print(ehab.to_string())
# print("for two", ehab.includes(2))
# print("for6", ehab.includes(6))
# print("for 3", ehab.includes(3))


