class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class binarytree:
    def __init__(self):
        self.root = None

    def inorder(self):
        """class method return a list of the object content as the following left>>root>>right and 
        takes no argument"""
        self.values = []
        if not self.root:
            return "empty tree"

        def ordering(node):
            if node.left:
                ordering(node.left)
            self.values += [node.value]
            if node.right:
                ordering(node.right)
            return self.values
        return ordering(self.root)

    def preorder(self):
        """class method return a list of the object(tree) contant as the following root>>left>>right and takes no argument"""
        self.values = []
        if self.root == None:
            return "empty tree"

        def ordering(node):

            self.values += [node.value]
            if node.left:
                ordering(node.left)
            if node.right:
                ordering(node.right)
            return self.values
        return ordering(self.root)

    def postorder(self):
        """class method return a list of the object(tree) contant as the following left>>right>>root and takes no argument"""
        self.values = []
        if not self.root:
            return "empty tree"

        def ordering(node):
            if node.left:
                ordering(node.left)
            if node.right:
                ordering(node.right)
            self.values += [node.value]
            return self.values
        return ordering(self.root)


class binarysearchtree(binarytree):
    def add(self, value):
        """a class method that add values to the tree either to the right or to the left based on wish value is greater the right or the left also depends on the root at the first level"""
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root
            while current:
                if value < current.value:
                    if current.left == None:
                        current.left = Node(value)
                        break
                    current = current.left

                else:
                    if current.right == None:
                        current.right = Node(value)
                        break
                    current = current.right

    def Contains(self, value):
        """class method takes one argument and check if this argument are within the tree content either on right or left and return that the vakue does exist in the tree or not"""
        if self.root == None:
            return 'empty tree'
        else:
            current = self.root
            while current:
                if current.value == value:
                    return "the value is exist"
                elif value < current.value:
                    if current.left == None:
                        return "dose not exist"
                    current = current.left
                else:
                    if current.right == None:
                        return "dose not exist"
                    current = current.right


ehab = binarysearchtree()
ehab.add(5)
ehab.add(3)
ehab.add(9)
ehab.add(2)
ehab.add(4)
ehab.add(7)
ehab.add(10)


#####################################################################
def breadth_first(tree):
    l = []
    if tree.root == None:
        return "empty tree"
    else:
        l.append(tree.root.value)

        def ordering(tree):

            if tree.left:
                l.append(tree.left.value)
            if tree.right:
                l.append(tree.right.value)
            if tree.left:
                ordering(tree.left)
            if tree.right:
                ordering(tree.right)

        ordering(tree.root)
        return l


print(breadth_first(ehab))
###############################################################
