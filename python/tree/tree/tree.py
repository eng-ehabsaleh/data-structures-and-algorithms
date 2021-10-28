class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class binarytree:
    def __init__(self):
        self.root = None

    def inorder(self):
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


if __name__ == '__main__':
    ehab = binarysearchtree()
    ehab.add(1)
    ehab.add(2)
    ehab.add(3)
    ehab.add(4)
    ehab.add(5)
    print(ehab.inorder())
    print(ehab.postorder())
    print(ehab.preorder())
    print(ehab.Contains(5))
    print(ehab.Contains(7))
