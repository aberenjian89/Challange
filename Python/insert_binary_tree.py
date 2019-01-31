class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root == None:
        return root
    current = root
    parent = None
    while current != None:
        parent = current
        if current.val > val:
            current = current.left
        else:
            current = current.right

    if parent.val > val:
        parent.left = TreeNode(val)
    else:
        parent.right = TreeNode(val)
    return root


def printTree(root):
    if root == None:
        return root
    printTree(root.left)
    print(root.val)
    printTree(root.right)


root = TreeNode(10)
root.left = TreeNode(2)
root.left.left = TreeNode(-1)
root.left.right = TreeNode(4)
root.right = TreeNode(12)


insert(root, 3)
printTree(root)
