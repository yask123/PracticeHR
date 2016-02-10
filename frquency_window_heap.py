class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        cache = {}
        for i in range(B):
            try:
                cache[A[i]] += 1
            except:
                cache[A[i]] = 1

        # We have solution for [0,B-1]
        # Now we need solution for [1,B][2,B+1]....
        result = []
        start = 1
        end = B
        result.append(self.calc_unique(cache))
        while (end < len(A)):

            cache[A[start - 1]] -= 1
            try:
                cache[A[end]] += 1
            except:
                cache[A[end]] = 1
            start += 1
            end += 1
            result.append(self.calc_unique(cache))
        return result

    def calc_unique(self, A):
        print A
        count = 0
        for each_key in A:
            if A[each_key] > 0:
                count += 1
        return count


a = Solution()
print a.dNums([1, 2, 1, 3, 4, 3], 3)
