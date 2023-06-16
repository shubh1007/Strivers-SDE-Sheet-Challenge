from typing import List
from sys import maxsize

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -maxsize
        curr_sum = -maxsize
        for i in nums:
            curr_sum += i
            max_sum = max(max_sum, curr_sum)
            curr_sum = max(0, curr_sum)
        return max_sum