import unittest

from algorithm_patterns.recursion.medium.power_x_n import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_pow_zero(self):
        # x^0 should always return 1
        self.assertEqual(self.sol.pow(2, 0), 1)
        self.assertEqual(self.sol.myPow(2, 0), 1)

    def test_pow_one(self):
        # x^1 should return x
        self.assertEqual(self.sol.pow(2, 1), 2)
        self.assertEqual(self.sol.myPow(2, 1), 2)

    def test_pow_two(self):
        # x^2 should return x*x
        self.assertEqual(self.sol.pow(3, 2), 9)
        self.assertEqual(self.sol.myPow(3, 2), 9)

    def test_positive_exponents(self):
        self.assertEqual(self.sol.myPow(2, 3), 8)
        self.assertEqual(self.sol.myPow(2, 4), 16)
        self.assertEqual(self.sol.myPow(3, 3), 27)
        self.assertEqual(self.sol.myPow(2, 10), 1024)

    def test_negative_exponents(self):
        self.assertAlmostEqual(self.sol.myPow(2, -3), 0.125)
        self.assertAlmostEqual(self.sol.myPow(2, -4), 0.0625)

    def test_fractional_base(self):
        self.assertAlmostEqual(self.sol.myPow(2.5, 3), 15.625)
        self.assertAlmostEqual(self.sol.myPow(2.5, -2), 0.16)

    def test_negative_base(self):
        self.assertEqual(self.sol.myPow(-2, 3), -8)
        self.assertEqual(self.sol.myPow(-2, 2), 4)


if __name__ == "__main__":
    unittest.main()
