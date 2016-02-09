'''
https://www.interviewbit.com/courses/programming/topics/arrays/problems/spiral1/
'''
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = []
top = 0
bottom = len(A) - 1
left = 0
right = len(A[0]) - 1

while top <= bottom and left <= right:

    # Traverse right
    for i in range(left, right + 1):
        result.append(A[top][i])
    top += 1

    # Traverse Down
    for i in range(top, bottom + 1):
        result.append(A[i][right])
    right -= 1

    # Traverse Left
    for i in range(right, left - 1, -1):
        result.append(A[bottom][i])
    bottom -= 1

    # Traverse Up
    for i in range(bottom, top - 1, -1):
        result.append(A[i][left])
    left += 1

print result
