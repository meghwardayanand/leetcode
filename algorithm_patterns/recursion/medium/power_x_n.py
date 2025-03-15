class Solution:

    def pow(self, x: float, n: int) -> float:
        result = 1
        if n == 0:
            return 1

        if n == 1:
            return x

        if n == 2:
            return x*x

        result = self.pow(x, n//2)
        result = self.pow(result, 2)

        if n % 2 != 0:
            result = result * x

        return result

    def myPow(self, x: float, n: int) -> float:
        isPositivePower = True if n >= 0  else False
        if n < 0:
            n = -1 * n

        result = self.pow(x, n)
        return result if isPositivePower else 1/result
