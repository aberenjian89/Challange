class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    head = ListNode(-1)
    prev = head
    carry = 0
    while (l1 != None or l2 != None):
        if l1 != None:
            x = l1.val
        else:
            x = 0
        if l2 != None:
            y = l2.val
        else:
            y = 0
        res = carry + x + y
        carry = int(res / 10)
        node = ListNode(res % 10)
        prev.next = node
        prev = prev.next
        l1 = l1.next if l1 != None else None
        l2 = l2.next if l2 != None else None

    if carry > 0:
        node = ListNode(carry)
        prev.next = node

    return head.next


def printlist(root):
    while (root != None):
        print(root.val)
        root = root.next


root1 = ListNode(2)
obj2 = ListNode(4)
obj3 = ListNode(3)

root1.next = obj2
obj2.next = obj3


root2 = ListNode(5)
obj3 = ListNode(6)
obj4 = ListNode(4)


root2.next = obj3
obj3.next = obj4


printlist((addTwoNumbers(root1, root2)))
