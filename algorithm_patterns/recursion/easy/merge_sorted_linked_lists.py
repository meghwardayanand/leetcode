
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, list1, list2, previous):
        if not list1:
            previous.next = list2
            return

        if not list2:
            previous.next = list1
            return

        if list1.val <= list2.val:
            previous.next = ListNode(list1.val)
            self.merge(list1.next, list2, previous.next)
        else:
            previous.next = ListNode(list2.val)
            self.merge(list1, list2.next, previous.next)

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not (list1 or list2):
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        if list1.val <= list2.val:
            new_list = ListNode(list1.val)
            self.merge(list1.next, list2, new_list)
        else:
            new_list = ListNode(list2.val)
            self.merge(list1, list2.next, new_list)

        return new_list
