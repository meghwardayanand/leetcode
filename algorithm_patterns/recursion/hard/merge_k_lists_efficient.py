from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, list1: List[Optional[ListNode]], list2: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.merge(list1.next, list2)
            return list1
        else:
            list2.next = self.merge(list1, list2.next)
            return list2

    def divide(self, lists: List[Optional[ListNode]], start: int, end: int) -> Optional[ListNode]:
        if start == end:
            return lists[start]

        mid = start + (end - start)//2
        list1 = self.divide(lists, start, mid)
        list2 = self.divide(lists, mid+1, end)
        return self.merge(list1, list2)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        size = len(lists)
        if size == 0:
            return None

        return self.divide(lists, 0, size - 1)
