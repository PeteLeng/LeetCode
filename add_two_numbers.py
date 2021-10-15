# Add two linked list
def add(l1, l2):
    res = []
    rem = 0
    while l1 or l2:
        d1 = l1.pop(0).value if l1 else 0
        d2 = l2.pop(0).value if l2 else 0
        res.append((d1+d2+rem)%10)
        rem = (d1+d2+rem)//10
    if rem:
        res.append(rem)
    return res


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add(l1, l2):
    # point_to_head = ListNode(0)
    # res = point_to_head.next
    is_head = 1
    rem = 0
    while l1 or l2:
        d1 = l1.val if l1 else 0
        d2 = l2.val if l2 else 0
        if is_head:
            head = ListNode((d1 + d2 + rem) % 10)
            tail = head
            is_head = 0
        else:
            tail.next = ListNode((d1 + d2 + rem) % 10)
            tail = tail.next
        rem = (d1 + d2 + rem) // 10

        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2

    if rem:
        tail.next = ListNode(rem)
    return head


if __name__ == '__main__':
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]

    # l1 = [0]
    # l2 = [0]

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    print(add(l1, l2))