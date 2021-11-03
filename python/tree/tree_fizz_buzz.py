def fizz_buzz_tree(tree):
    new_tree = []
    if tree.root == None:
        return "empty tree"
    else:

        def ordering(root):
            if root.value % 3 == 0 and root.value % 5 == 0:
                new_tree.append("FizzBuzz")
            elif root.value % 3 == 0:
                new_tree.append("Fizz")
            elif root.value % 5 == 0:
                new_tree.append("Buzz")
            else:
                new_tree.append(str(root.value))

            if root.left:
                ordering(root.left)
            if root.right:
                ordering(root.right)
        ordering(tree.root)
        return new_tree
