class Solution:
    # @param A : tuple of integers
    # @return an integer
    '''
    Given the array [-2,1,-3,4,-1,2,1,-5,4],

    the contiguous subarray [4,-1,2,1] has the largest sum = 6.
    '''

    def maxSubArray(self, A):
        current_max = 0
        total_max = 0
        max_number_in_list = A[0]
        for i in range(len(A)):
            if A[i] > max_number_in_list:
                max_number_in_list = A[i]

            if A[i] + current_max >= 0:
                current_max += A[i]

                if total_max < current_max:
                    total_max = current_max
            else:
                current_max = 0
        if total_max > 0:
            return total_max
        else:
            return max_number_in_list


a = Solution()
print a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
