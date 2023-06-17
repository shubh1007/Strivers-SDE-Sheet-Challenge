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
        