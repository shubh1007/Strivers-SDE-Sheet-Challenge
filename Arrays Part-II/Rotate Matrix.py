# Approach:
# Step 1: Transpose the matrix. (transposing means changing columns to rows and rows to columns)
# Step 2: Reverse each row of the matrix.
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row of the matrix
        for row in range(n):
            matrix[row].reverse()
    
def rotateMatrix(mat, n, m):
    top, left, right, bottom = 0, 0, m - 1, n - 1
    while left < right and top < bottom:
        prev = mat[top + 1][left]
        
        for i in range(left, right + 1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
        top += 1

        for i in range(top, bottom + 1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr
        right -= 1

        for i in range(right, left - 1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
        left += 1
    

mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]
rotateMatrix(mat, 4, 4)
for i in mat:
    for j in i:
        print(j, end = "\t")
    print()