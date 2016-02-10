class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A, cache={}):
        if A in cache:
            return cache[A]

        if A == 0:
            return 1
        if A < 0:
            return 0

        cache[A] = self.climbStairs(A - 1) + self.climbStairs(A - 2)
        return cache[A]
