class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def coin_distributer(root, count):
    if root == None:
        return 0

    left = coin_distributer(root.left, count)
    right = coin_distributer(root.right, count)
    count = abs(left) + abs(right)
    return root.val + count - 1


root = Node(0)
root.left = Node(3)
root.right = Node(0)

print(coin_distributer(root, 0))
