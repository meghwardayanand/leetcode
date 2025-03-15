import unittest

from algorithm_patterns.recursion.merge_sorted_linked_lists import ListNode, Solution


def list_to_linked_list(lst):
    """Helper function to create a linked list from a Python list."""
    if not lst:
        return None

    head = ListNode(lst[0])
    current = head

    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def linked_list_to_list(node):
    """Helper function to convert a linked list back into a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next

    return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_both_null(self):
        list1 = None
        list2 = None
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertIsNone(result)

    def test_both_empty(self):
        list1 = []
        list2 = []
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [])

    def test_first_null(self):
        list1 = None
        list2 = list_to_linked_list([1, 2, 3])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_second_null(self):
        list1 = list_to_linked_list([1, 2, 3])
        list2 = None
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_normal_merge(self):
        list1 = list_to_linked_list([1, 3, 5])
        list2 = list_to_linked_list([2, 4, 6])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5, 6])

    def test_duplicates(self):
        list1 = list_to_linked_list([1, 3, 3, 5])
        list2 = list_to_linked_list([2, 3, 4])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 3, 3, 4, 5])

    def test_all_left_smaller(self):
        list1 = list_to_linked_list([1, 2, 3])
        list2 = list_to_linked_list([4, 5, 6])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5, 6])

    def test_all_left_larger(self):
        list1 = list_to_linked_list([4, 5, 6])
        list2 = list_to_linked_list([1, 2, 3])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5, 6])

    def test_one_empty_one_element(self):
        list1 = list_to_linked_list([])
        list2 = list_to_linked_list([0])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [0])

    def test_some_common_elements(self):
        list1 = list_to_linked_list([1, 2, 4])
        list2 = list_to_linked_list([1, 3, 4])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 1, 2, 3, 4, 4])


if __name__ == "__main__":
    unittest.main()
