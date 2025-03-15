from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        heads = [head for head in lists if head]
        def getSmallestNumber(heads):
            smallest_idx = 0
            smallest_value = None
            for idx, head in enumerate(heads):
                if not head:
                    continue

                if smallest_value is None:
                    smallest_value = head.val
                    smallest_idx = idx
                elif smallest_value > head.val:
                    smallest_value = head.val
                    smallest_idx = idx

            return smallest_idx, smallest_value

        smallest_idx, smallest_value = getSmallestNumber(heads)

        if smallest_value is None:
            return None

        new_list = ListNode(smallest_value)
        current_node = new_list
        heads[smallest_idx] = heads[smallest_idx].next
        while len(heads) > 0 and any(heads):
            smallest_idx, smallest_value = getSmallestNumber(heads)
            if smallest_value is not None:
                new_node = ListNode(smallest_value)
                current_node.next = new_node
                current_node = new_node
                heads[smallest_idx] = heads[smallest_idx].next

        return new_list
