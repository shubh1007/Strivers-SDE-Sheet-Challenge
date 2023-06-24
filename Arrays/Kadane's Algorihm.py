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
    

# CODING NINJAS
def maxSubarraySum(arr, n) :
    curr_sum = 0
    max_sum = - maxsize - 1
	# Your code here
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    # return the answer
    return max(0, max_sum)