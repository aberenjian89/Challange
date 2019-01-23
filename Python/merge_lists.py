class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge(l1, l2):
    head = ListNode(-1)
    prev = head
    while (l1 != None and l2 != None):
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    if l1 != None:
        prev.next = l1
    if l2 != None:
        prev.next = l2
    return head.next


def printlist(root):
    while (root != None):
        print(root.val)
        root = root.next


root1 = ListNode(1)
obj2 = ListNode(2)
obj3 = ListNode(4)

root1.next = obj2
obj2.next = obj3

root2 = ListNode(1)
obj4 = ListNode(3)
obj5 = ListNode(4)

root2.next = obj4
obj4.next = obj5

printlist(merge(root1, root2))
