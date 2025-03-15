import unittest

from algorithm_patterns.recursion.hard.permutation_sequence import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        # For n=3, permutations in order are:
        # "123", "132", "213", "231", "312", "321".
        # k=1 should return "123".
        self.assertEqual(self.sol.getPermutation(3, 1), "123")

    def test_case_2(self):
        # k=2 should return "132".
        self.assertEqual(self.sol.getPermutation(3, 2), "132")

    def test_case_3(self):
        # k=3 should return "213".
        self.assertEqual(self.sol.getPermutation(3, 3), "213")

    def test_case_4(self):
        # k=4 should return "231".
        self.assertEqual(self.sol.getPermutation(3, 4), "231")

    def test_case_5(self):
        # k=5 should return "312".
        self.assertEqual(self.sol.getPermutation(3, 5), "312")

    def test_case_6(self):
        # k=6 should return "321".
        self.assertEqual(self.sol.getPermutation(3, 6), "321")

    def test_case_7(self):
        # For n=4, there are 24 permutations.
        # A known example: for n=4 and k=9, the kth permutation is "2314".
        self.assertEqual(self.sol.getPermutation(4, 9), "2314")

    def test_larger_sequence(self):
        self.assertEqual(self.sol.getPermutation(9, 5040), "129876543")

    def test_one(self):
        self.assertEqual(self.sol.getPermutation(1, 1), "1")


if __name__ == '__main__':
    unittest.main()
