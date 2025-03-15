class Solution:
    def __init__(self):
        self.factorials = {
            0: 1,
            1: 1,
            2: 2,
            3: 6,
            4: 24,
            5: 120,
            6: 720,
            7: 5040,
            8: 40320,
            9: 362880
        }

    def factorial(self, x):
        if x == 1:
            return 1
        else:
            return x*self.factorial(x-1)

    def permute(self, sequence, nums, n, k):
        if k == 1:
            for num in nums:
                sequence += str(num)

            return sequence
        else:
            factorial = self.factorials[n - 1] # self.factorical(n-1) for larger numbers
            index = k // factorial
            if (k%factorial == 0):
                index -= 1

            number = nums.pop(index)
            sequence += str(number)
            k = k - factorial*index
            n = n - 1

            return self.permute(sequence, nums, n, k)

    def getPermutation(self, n: int, k: int) -> str:
        """
            n: blocks
            j --> (n - 1)!: no of elements in each block
            i --> k/j!: this indexed block contains our permutation
            ith element is our character
            other elements are: A[:i] + A[i+1:]
            new_n = n - 1
            k = k - j*i
            k - (i*j) is our new number in the selected block.
        """
        nums = list(range(1, n+1))
        sequence = ""
        return self.permute(sequence, nums, n, k)
