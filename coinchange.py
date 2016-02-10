class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, A, B):
        if B == 0:
            return 1
        if B < 0:
            return 0
        if len(A) == 0:
            return 0
        return self.coinchange2(A, B - A[-1]) + self.coinchange2(A[:-1], B)


a = Solution()
a.coinchange2([1, 2, 3], 4)
