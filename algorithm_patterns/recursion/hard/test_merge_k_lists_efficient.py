import unittest
from typing import List, Optional

from algorithm_patterns.recursion.hard.merge_k_lists_efficient import ListNode, Solution


def list_to_linked_list(list: List[int]) -> Optional[ListNode]:
    """Converts a Python list to a linked list."""
    if not list:
        return None

    head = ListNode(list[0])
    current = head
    for value in list[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    """Converts a linked list back into a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next

    return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_input(self):
        self.assertIsNone(self.solution.mergeKLists([]))

    def test_all_empty(self):
        lists = [None, None, None]
        self.assertIsNone(self.solution.mergeKLists(lists))

    def test_single_list(self):
        l1 = list_to_linked_list([1, 3, 5])
        result = self.solution.mergeKLists([l1])
        self.assertEqual(linked_list_to_list(result), [1, 3, 5])

    def test_multiple_lists(self):
        l1 = list_to_linked_list([1, 4, 5])
        l2 = list_to_linked_list([1, 3, 4])
        l3 = list_to_linked_list([2, 6])
        result = self.solution.mergeKLists([l1, l2, l3])
        self.assertEqual(linked_list_to_list(result), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_mixed_empty_and_nonempty(self):
        l1 = list_to_linked_list([2, 4, 6])
        l2 = None
        l3 = list_to_linked_list([1, 3, 5])
        result = self.solution.mergeKLists([l1, l2, l3])
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5, 6])

    def test_duplicate_values(self):
        l1 = list_to_linked_list([1, 3, 5])
        l2 = list_to_linked_list([1, 3, 5])
        result = self.solution.mergeKLists([l1, l2])
        self.assertEqual(linked_list_to_list(result), [1, 1, 3, 3, 5, 5])


if __name__ == "__main__":
    unittest.main()
