from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp = []
        for row in matrix:
            for col in row:
                temp.append(col)
        low = 0
        high = len(temp) - 1
        while low <= high:
            mid = (low + high) // 2
            if temp[mid] == target:
                return True
            elif temp[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
